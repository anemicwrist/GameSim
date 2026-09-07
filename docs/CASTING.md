# Desktop to TV

The Orgo desktop is a VNC stream. Your Windows PC views it, and the TV shows
what the Windows PC is showing. There is no code in this repo for this step.

## View the desktop

Open the computer in the Orgo web app and go fullscreen (F11). Any
websockify-capable VNC client also works, connecting to:

```
wss://www.orgo.ai/desktops/<instance_id>/ws/websockify?token=<password>
```

The browser is the simpler option and is what the casting instructions assume.

Set the Flycast window to fullscreen so the game fills the 1280x720 desktop.
`scripts/configure_flycast.py` already sets `fullscreen = yes`.

## Cast it

**Chromecast, or a TV with Chromecast built in.** In Chrome, the three-dot menu,
then Cast. Choose the TV, and in the Sources dropdown pick **Cast tab** with the
Orgo viewer tab active. "Cast tab" tracks a single tab and is generally smoother
than "Cast desktop".

**Miracast, most Windows-compatible smart TVs.** Press `Win + K`, pick the TV,
and choose Duplicate. Then fullscreen the browser.

**AirPlay, Apple TV or an AirPlay 2 TV.** Windows has no built-in AirPlay
sender. Use a third-party sender, or connect an HDMI cable instead.

**HDMI cable.** If the Windows PC can reach the TV with a cable, use it. It
removes 60-200 ms and a whole class of dropout problems.

## Sound

Orgo's desktop stream carries no audio, so the game's sound does not reach the
Windows PC and therefore does not reach the TV. Nothing in the casting setup
changes this.

If you want sound, you need a different stream out of the VM entirely. Sunshine
on the Orgo computer plus Moonlight on the Windows PC carries video and audio
together, and at a much better frame rate than VNC. It is more setup and it
costs CPU on the VM, so it is worth doing only if VNC turns out to be the thing
that spoils the session. There is a sketch of it in
`docs/TROUBLESHOOTING.md` under "the video is too choppy".

## Expectations

VNC of a 60 fps game over the internet is not 60 fps. Expect something between
15 and 30 fps at 1280x720, lower when the screen is busy, which in Marvel vs
Capcom 2 is most of the time. The game itself still runs at full speed on the
VM; it is the picture that is thinned out.
