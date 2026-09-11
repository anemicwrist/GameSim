<#
.SYNOPSIS
  Starts the pad server and launches the game.

.DESCRIPTION
  Run this each time you want to play. It picks the same backend
  scripts\setup_windows.ps1 found, starts the pad server, prints the URL for the
  phones, and launches the emulator. Closing the emulator stops the server.

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File scripts\run.ps1
  powershell -ExecutionPolicy Bypass -File scripts\run.ps1 -Game C:\dumps\mvc2.gdi
#>
[CmdletBinding()]
param(
    [string]$Game,
    [int]$Port = 8080,
    [int]$Players = 2,
    [string]$Token = '',
    [ValidateSet('auto', 'vigem', 'winkey')]
    [string]$Backend = 'auto',
    [string]$Emulator,
    [switch]$Tunnel
)

$ErrorActionPreference = 'Stop'
$RepoDir = Split-Path -Parent $PSScriptRoot

function Write-Step($text) { Write-Host "==> $text" -ForegroundColor Cyan }
function Fail($text) { Write-Host "error: $text" -ForegroundColor Red; exit 1 }

$venvPython = Join-Path $RepoDir '.venv\Scripts\python.exe'
if (-not (Test-Path $venvPython)) {
    Fail 'no virtual environment. Run scripts\setup_windows.ps1 first.'
}

# A tunnel address is public: anyone who has it could otherwise play your
# player 2. Require a shared secret, and invent one if none was given.
if ($Tunnel -and -not $Token) {
    $Token = -join ((48..57) + (97..122) | Get-Random -Count 10 |
        ForEach-Object { [char]$_ })
    Write-Host "generated a URL secret for the tunnel: $Token" -ForegroundColor Yellow
}

if ($Emulator -and -not (Test-Path $Emulator)) {
    Fail "no such emulator: $Emulator"
}

# --- the game ----------------------------------------------------------------
if (-not $Game) {
    $gamesDir = Join-Path $RepoDir 'games'
    if (Test-Path $gamesDir) {
        $Game = Get-ChildItem -Path $gamesDir -Recurse -File -Depth 3 |
            Where-Object { $_.Extension -in '.gdi', '.chd', '.cdi', '.cue', '.m3u' } |
            Sort-Object FullName | Select-Object -First 1 -ExpandProperty FullName
    }
}
if (-not $Game -or -not (Test-Path $Game)) {
    Fail @"
no game file found.

Put your own Marvel vs Capcom 2 dump (.gdi/.chd/.cdi) in:
  $(Join-Path $RepoDir 'games')
or pass it: scripts\run.ps1 -Game C:\path\to\mvc2.gdi
See docs\GAME_FILES.md.
"@
}

# --- backend -----------------------------------------------------------------
if ($Backend -eq 'auto') {
    $vigemDriver = Get-CimInstance Win32_SystemDriver -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -like '*ViGEm*' }
    $Backend = if ($vigemDriver) { 'vigem' } else { 'winkey' }
}
Write-Step "input backend: $Backend"

# --- pad server --------------------------------------------------------------
Write-Step "starting padserver on port $Port"
$padArgs = @('-m', 'padserver', '--backend', $Backend, '--port', $Port, '--players', $Players)
if ($Token) { $padArgs += @('--token', $Token) }

$padProcess = Start-Process -FilePath $venvPython -ArgumentList $padArgs `
    -PassThru -NoNewWindow

try {
    $ready = $false
    foreach ($attempt in 1..50) {
        Start-Sleep -Milliseconds 200
        try {
            Invoke-WebRequest -Uri "http://127.0.0.1:$Port/health" -UseBasicParsing `
                -TimeoutSec 2 | Out-Null
            $ready = $true
            break
        } catch { }
    }
    if (-not $ready) { Fail "padserver did not come up on port $Port" }

    # --- where the phones should point ---------------------------------------
    $suffix = if ($Token) { "?k=$Token" } else { '' }

    if ($Tunnel) {
        # cloudflared dials out, so this works behind a firewall that refuses
        # inbound connections and needs no administrator rights. It is a single
        # executable: nothing is installed and nothing is left on the machine
        # except the file itself, inside this repo.
        $cloudflared = Join-Path $RepoDir 'cloudflared.exe'
        if (-not (Test-Path $cloudflared)) {
            $onPath = Get-Command cloudflared -ErrorAction SilentlyContinue
            if ($onPath) {
                $cloudflared = $onPath.Source
            } else {
                Write-Step 'fetching cloudflared (one file, nothing installed)'
                $url = 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe'
                try {
                    Invoke-WebRequest -Uri $url -OutFile $cloudflared -UseBasicParsing
                } catch {
                    Fail @"
could not download cloudflared.

Get it manually from https://github.com/cloudflare/cloudflared/releases
and save it as: $cloudflared
"@
                }
            }
        }

        Write-Step 'opening the tunnel'
        $tunnelLog = Join-Path $env:TEMP "gamesim-tunnel-$PID.log"
        $tunnelProcess = Start-Process -FilePath $cloudflared `
            -ArgumentList @('tunnel', '--url', "http://localhost:$Port") `
            -PassThru -NoNewWindow -RedirectStandardError $tunnelLog

        $publicUrl = $null
        foreach ($attempt in 1..60) {
            Start-Sleep -Milliseconds 500
            if (Test-Path $tunnelLog) {
                $match = Select-String -Path $tunnelLog -Pattern 'https://[-\w]+\.trycloudflare\.com' `
                    -ErrorAction SilentlyContinue | Select-Object -First 1
                if ($match) {
                    $publicUrl = $match.Matches[0].Value
                    break
                }
            }
            if ($tunnelProcess.HasExited) { break }
        }

        Write-Host ''
        if ($publicUrl) {
            Write-Host 'Phones open:' -ForegroundColor Green
            Write-Host "  $publicUrl/$suffix"
            Write-Host ''
            Write-Host '  (this address is public but unguessable, and the secret above'
            Write-Host '   is required; it stops working when you close the game)'
        } else {
            Write-Host 'The tunnel did not report an address.' -ForegroundColor Yellow
            Write-Host "  see $tunnelLog"
        }
        Write-Host ''
    } else {
        Write-Host ''
        Write-Host 'Phones open:' -ForegroundColor Green
        Get-NetIPAddress -AddressFamily IPv4 -ErrorAction SilentlyContinue |
            Where-Object {
                $_.IPAddress -notlike '127.*' -and $_.IPAddress -notlike '169.254.*'
            } |
            ForEach-Object { Write-Host "  http://$($_.IPAddress):$Port/$suffix" }
        if (Get-Command tailscale -ErrorAction SilentlyContinue) {
            $ts = & tailscale ip -4 2>$null | Select-Object -First 1
            if ($ts) { Write-Host "  http://${ts}:$Port/$suffix   (tailscale)" }
        }
        Write-Host ''
        Write-Host '  (if the phones cannot reach these, the firewall is blocking them:'
        Write-Host '   re-run with -Tunnel, which needs no firewall change)'
        Write-Host ''
    }

    # --- the emulator --------------------------------------------------------
    if (-not $Emulator) {
        $names = if ($Backend -eq 'vigem') { @('flycast.exe') } else { @('retroarch.exe') }
        $searchRoots = @(
            $RepoDir,
            "$env:LOCALAPPDATA\Programs",
            "$env:ProgramFiles",
            "${env:ProgramFiles(x86)}"
        ) | Where-Object { $_ -and (Test-Path $_) }

        foreach ($name in $names) {
            $found = Get-Command $name -ErrorAction SilentlyContinue
            if ($found) { $Emulator = $found.Source; break }
            foreach ($root in $searchRoots) {
                # Bounded depth: an unbounded recurse through Program Files can
                # take minutes, which is a poor way to start game night.
                $hit = Get-ChildItem -Path $root -Filter $name -Recurse -File `
                    -Depth 3 -ErrorAction SilentlyContinue | Select-Object -First 1
                if ($hit) { $Emulator = $hit.FullName; break }
            }
            if ($Emulator) { break }
        }
    }
    if (-not $Emulator) {
        $want = if ($Backend -eq 'vigem') { 'Flycast' } else { 'RetroArch' }
        $exe = if ($Backend -eq 'vigem') { 'flycast.exe' } else { 'retroarch.exe' }
        Fail @"
could not find $want.

Install it, or pass the path: scripts\run.ps1 -Emulator "C:\path\to\$exe"
See docs\WINDOWS.md.
"@
    }

    Write-Step "launching $(Split-Path -Leaf $Emulator)"
    Write-Host "    game: $Game"
    if ($Backend -eq 'vigem') {
        Start-Process -FilePath $Emulator -ArgumentList @($Game) -Wait
    } else {
        # RetroArch needs the core told to it explicitly.
        $core = Get-ChildItem -Path (Split-Path -Parent $Emulator) -Recurse -File `
            -Filter 'flycast_libretro.dll' -ErrorAction SilentlyContinue |
            Select-Object -First 1
        if (-not $core) {
            Fail @"
RetroArch is installed but the Flycast core is missing.

In RetroArch: Online Updater > Core Downloader > Sega Dreamcast (Flycast)
"@
        }
        Start-Process -FilePath $Emulator `
            -ArgumentList @('-L', "`"$($core.FullName)`"", '-f', "`"$Game`"") -Wait
    }
} finally {
    if ($tunnelProcess -and -not $tunnelProcess.HasExited) {
        Write-Step 'closing the tunnel'
        Stop-Process -Id $tunnelProcess.Id -Force -ErrorAction SilentlyContinue
    }
    if ($padProcess -and -not $padProcess.HasExited) {
        Write-Step 'stopping padserver'
        Stop-Process -Id $padProcess.Id -Force -ErrorAction SilentlyContinue
    }
}
