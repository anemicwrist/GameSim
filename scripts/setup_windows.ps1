<#
.SYNOPSIS
  Sets up GameSim on Windows and works out how input can reach the emulator.

.DESCRIPTION
  There are two ways in on Windows.

  vigem   Virtual Xbox 360 pads through the ViGEmBus driver. The better option:
          each player is a real separate device and standalone Flycast works.
          Installing the driver needs administrator rights.

  winkey  Synthetic key presses through the Win32 SendInput API. Needs no
          driver, no administrator rights and no install beyond Python, so it
          works on a managed or work-owned machine. Both players share one
          keyboard, so the emulator is RetroArch with the Flycast core.

  This script detects which is available and installs accordingly. Everything it
  creates lives inside this repository folder, so removing the folder removes
  almost all of it; see docs/WINDOWS.md for the short cleanup list.

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File scripts\setup_windows.ps1
#>
[CmdletBinding()]
param(
    [int]$Port = 8080,
    [ValidateSet('auto', 'vigem', 'winkey')]
    [string]$Backend = 'auto'
)

$ErrorActionPreference = 'Stop'
$RepoDir = Split-Path -Parent $PSScriptRoot

function Write-Step($text) { Write-Host "==> $text" -ForegroundColor Cyan }
function Write-Warn($text) { Write-Host "!!  $text" -ForegroundColor Yellow }

# --- python ------------------------------------------------------------------
Write-Step 'looking for Python'
$python = $null
foreach ($candidate in @('py -3', 'python', 'python3')) {
    $parts = $candidate.Split(' ')
    $exe = Get-Command $parts[0] -ErrorAction SilentlyContinue
    if ($exe) { $python = $candidate; break }
}
if (-not $python) {
    Write-Warn 'Python was not found.'
    Write-Host '    Install it from https://www.python.org/downloads/ or the Microsoft Store.'
    Write-Host '    The Store version needs no administrator rights, which helps on a work machine.'
    exit 1
}
$version = & ([scriptblock]::Create("$python --version")) 2>&1
Write-Host "    $version"

# --- virtual environment, inside the repo so nothing leaks onto the machine ---
Write-Step 'creating the virtual environment'
$venv = Join-Path $RepoDir '.venv'
if (-not (Test-Path $venv)) {
    & ([scriptblock]::Create("$python -m venv `"$venv`""))
}
$venvPython = Join-Path $venv 'Scripts\python.exe'
if (-not (Test-Path $venvPython)) {
    Write-Warn "the virtual environment was not created at $venv"
    exit 1
}
& $venvPython -m pip install --quiet --upgrade pip
& $venvPython -m pip install --quiet -e $RepoDir

# --- which backend can this machine use? -------------------------------------
Write-Step 'checking what this machine allows'

$identity = [Security.Principal.WindowsIdentity]::GetCurrent()
$isAdmin = ([Security.Principal.WindowsPrincipal]$identity).IsInRole(
    [Security.Principal.WindowsBuiltInRole]::Administrator)
Write-Host "    administrator: $(if ($isAdmin) { 'yes' } else { 'no' })"

$vigemDriver = Get-CimInstance Win32_SystemDriver -ErrorAction SilentlyContinue |
    Where-Object { $_.Name -like '*ViGEm*' }
$hasVigem = [bool]$vigemDriver
Write-Host "    ViGEmBus driver: $(if ($hasVigem) { 'installed' } else { 'not installed' })"

if ($Backend -eq 'auto') {
    $Backend = if ($hasVigem) { 'vigem' } else { 'winkey' }
    Write-Host "    chosen backend: $Backend"
} else {
    Write-Host "    chosen backend: $Backend (forced)"
}

if ($Backend -eq 'vigem' -and -not $hasVigem) {
    Write-Warn 'vigem was requested but the ViGEmBus driver is not installed.'
    Write-Host '    Get it from https://github.com/nefarius/ViGEmBus/releases'
    Write-Host '    Installing it needs administrator rights.'
    exit 1
}

# --- backend dependencies ----------------------------------------------------
Write-Step "installing dependencies for the '$Backend' backend"
if ($Backend -eq 'vigem') {
    & $venvPython -m pip install --quiet -e "$RepoDir[vigem]"
} else {
    Write-Host '    winkey uses the standard library only; nothing to install.'
}

# --- firewall ----------------------------------------------------------------
Write-Step "allowing the phones to reach port $Port"
$ruleName = 'GameSim padserver'
$existing = Get-NetFirewallRule -DisplayName $ruleName -ErrorAction SilentlyContinue
if ($existing) {
    Write-Host '    firewall rule already present'
} elseif ($isAdmin) {
    New-NetFirewallRule -DisplayName $ruleName -Direction Inbound `
        -LocalPort $Port -Protocol TCP -Action Allow -Profile Private | Out-Null
    Write-Host '    firewall rule added for private networks'
} else {
    Write-Warn "cannot add a firewall rule without administrator rights."
    Write-Host '    Try it anyway: Windows often prompts to allow Python the first time,'
    Write-Host '    and on a private network it may work with no rule at all.'
    Write-Host ''
    Write-Host '    If the phones cannot connect, use a tunnel instead. It makes an'
    Write-Host '    OUTBOUND connection, so it needs no firewall change at all:'
    Write-Host '      cloudflared tunnel --url http://localhost:' -NoNewline
    Write-Host $Port
    Write-Host '    See docs/WINDOWS.md, "when the firewall is locked down".'
}

# --- emulator config ---------------------------------------------------------
if ($Backend -eq 'winkey') {
    Write-Step 'writing two-player key bindings for RetroArch'
    & $venvPython (Join-Path $RepoDir 'scripts\configure_retroarch.py')
}

# --- what next ---------------------------------------------------------------
Write-Host ''
Write-Host "done. This machine will use the '$Backend' backend." -ForegroundColor Green
Write-Host ''
if ($Backend -eq 'vigem') {
    Write-Host 'Install Flycast for Windows:  https://flycast.org/  (or GitHub releases)'
    Write-Host 'Two virtual Xbox 360 pads will appear when you start the server.'
} else {
    Write-Host 'Install RetroArch:  https://retroarch.com/  then use'
    Write-Host '  Online Updater > Core Downloader > Sega Dreamcast (Flycast)'
    Write-Host 'Both players share one keyboard, with bindings already written.'
}
Write-Host ''
Write-Host "Put your game dump in:  $(Join-Path $RepoDir 'games')"
Write-Host 'Then run:  powershell -ExecutionPolicy Bypass -File scripts\run.ps1'
