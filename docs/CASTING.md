# Getting the picture onto the TV

The game runs on the Windows tablet, so this step mirrors **a local window**,
not a remote desktop. That matters: the picture is generated right where it is
being sent from, at full frame rate, and **the sound comes with it**. The old
Orgo arrangement could not carry audio at all.

Two ways across, and they are not close in quality.

## Best: a cable, if your tablet can do it

The tablet has no HDMI socket, but that is not the same as having no video out.
Most machines with Intel Iris Xe graphics expose **DisplayPort alt mode over
USB-C**, which a cheap USB-C-to-HDMI adapter turns into an ordinary HDMI
output. Work docks very often have one already.

Check before assuming otherwise:

- Look for the DisplayPort logo (a "D" containing a "P") or a Thunderbolt bolt
  next to the USB-C port.
- Or plug in any USB-C-to-HDMI adapter and see whether the TV finds a signal.
- Or run `dxdiag`, save the report, and look for an output listed on the
  display adapter.

If it works, use it. It removes 60-200 ms of latency, every dropout, all the
compression artefacts, and the entire class of "the TV stopped seeing the
tablet" problems. It is the single biggest improvement available to this setup
and it costs about ten dollars.

## Otherwise: Miracast to the Roku TV

Roku TVs accept Miracast, which is what Windows uses.

**On the Roku**, once: Settings → System → Screen mirroring → Screen mirroring
mode → **Prompt** or **Always allow**.

**On the tablet**, each time:

1. `Win` + `K`
2. Pick the TV from the list
3. Choose **Duplicate** (not Extend, or the game will open on the wrong screen)
4. Accept the prompt on the TV with the Roku remote if you chose Prompt

Then start the game and put it fullscreen.

### Making Miracast as good as it gets

Miracast quality varies enormously with conditions, and these are worth doing:

- **Use 5 GHz Wi-Fi**, not 2.4 GHz. This is the single biggest factor.
- **Put the tablet near the TV.** Miracast is a direct radio link between the
  two devices, so walls between them matter more than distance to your router.
- **Close everything else on the tablet.** Miracast encoding is real work, and
  it competes with the emulator for the same GPU.
- **Plug the tablet in.** Windows power saving throttles both the GPU and the
  radio on battery.
- **Run the game at 720p rather than 1080p.** Fewer pixels to encode means
  lower latency, and the game is 640x480 internally regardless.

### Expectations

Expect 60-200 ms of display lag, on top of a picture that is noticeably
compressed when the screen is busy — which in this game is most of the time.

Importantly, this is *display* lag, not *input* lag. Your inputs reach the
emulator over your own wifi in single-digit milliseconds, and the game logic
responds immediately. Everything is simply shown a moment late, uniformly.
That is far easier to adapt to than input lag, and it is the main reason this
setup is worth playing while the all-cloud version was not.

## Sound

Miracast carries audio along with video, so the game's sound comes out of the
TV. If it does not:

- Windows may have left the tablet's speakers as the output device. Click the
  volume icon and select the TV.
- Some Roku models mute mirrored audio until the TV's own volume is raised.

## If you are running on Orgo instead

The Orgo path is the fallback, documented in `docs/ORGO_SETUP.md`. It works
differently: the game runs in the cloud and you are mirroring a **VNC stream**
of a remote desktop.

Open the computer in the Orgo web app and press F11 for fullscreen, then cast
that browser window as above. Any websockify-capable VNC client also works:

```
wss://www.orgo.ai/desktops/<instance_id>/ws/websockify?token=<password>
```

Two things are worse on that path, and neither can be fixed from the casting
end. **There is no sound at all**, because Orgo's stream carries no audio. And
VNC of a 60 fps game over the internet is not 60 fps: expect 15-30 fps at
1280x720, lower when the screen is busy. The game runs at full speed on the VM;
it is the picture that is thinned out.
