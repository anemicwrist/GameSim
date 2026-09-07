# Getting the phones to the pad server

The Orgo computer has no public inbound address, so `http://<vm-ip>:8080` does
not work from your phone. Two ways around that.

## Tailscale, recommended

Tailscale builds a private encrypted network between your devices. Nothing is
exposed to the internet, and the phone-to-VM path is usually direct rather than
relayed, which keeps the latency down.

On the Orgo computer:

```bash
bash scripts/install_tailscale.sh
```

It prints a login URL. Open it, sign in, approve the machine, and it prints the
VM's tailnet address (a `100.x.y.z` address).

On each phone: install the Tailscale app from Play, sign in with the same
account, and turn the VPN on. Then open Chrome and go to:

```
http://100.x.y.z:8080/
```

Add your Windows PC to the same tailnet too. It makes moving the game dump
across easy, and it is what Moonlight would use if you go that route later.

### Checking the path is direct

```bash
tailscale status
```

A line reading `direct 203.0.113.5:41641` for a phone means peer-to-peer. A line
reading `relay "sea"` means traffic is going through a Tailscale relay, which
adds tens of milliseconds. Relays usually appear when one side is on a
restrictive mobile network; switching the phone to your home wifi normally fixes
it.

## Cloudflare tunnel, fallback

If you would rather not install anything on the phones, this gives the pad
server a temporary public HTTPS URL. Anyone with the URL can take a player slot,
so use a token.

```bash
PADSERVER_TOKEN=pick-something-random bash scripts/run.sh   # terminal 1
bash scripts/tunnel.sh                                      # terminal 2
```

`tunnel.sh` prints a `https://<random-words>.trycloudflare.com` URL. The phones
open that URL with the token on the end:

```
https://<random-words>.trycloudflare.com/?k=pick-something-random
```

Without the correct `?k=`, the page and the WebSocket both return 403. The URL
changes every time you start the tunnel, and the hop through Cloudflare's
network costs you some latency.

## The pad server's own options

```
--port 8080          listen port
--token SECRET       require ?k=SECRET on the page and the socket
--players 2          number of pads to create
--backend uinput     uinput (Linux), vigem (Windows), fake (no devices)
--no-analog          drive only the d-pad, leave the analog stick centred
```

`http://127.0.0.1:8080/status` on the VM shows which slots are taken, how many
input messages each has sent, and the current button state of each pad. It is
the quickest way to tell whether a phone's input is arriving at all.
