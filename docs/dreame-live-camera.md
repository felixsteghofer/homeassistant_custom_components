# Dreame Live Camera

[Source and full guide](https://github.com/felixsteghofer/dreame-live-camera) ·
[Releases](https://github.com/felixsteghofer/dreame-live-camera/releases) ·
[Issues](https://github.com/felixsteghofer/dreame-live-camera/issues)

Adds a native live camera and Start/Stop buttons for compatible Dreame/MOVA vacuum
cameras. Domain: `dreame_live_camera`. The existing `dreame_vacuum` integration
provides the authenticated device transport; this component does not replace it.

## Setup

1. Configure the supported vacuum in `Tasshack/dreame-vacuum` first.
2. Add `felixsteghofer/dreame-live-camera` to HACS as **Integration**, download it,
   restart HA, and add **Dreame Live Camera** under Devices & services.
3. Select the existing vacuum and provide its camera PIN. Configure the session
   limit through integration options; keep PINs out of dashboard configuration.
4. Close the manufacturer's live viewer before starting an HA session. Use the
   camera and Start/Stop buttons, or configure its entity in Dahoam Vacuum Card.

Preview requests do not start monitoring. Sessions have a duration limit and viewer
cleanup; use Stop if a client retains a stream connection after closing its viewer.
Cloud authentication/signaling/control is still required even with direct LAN video.
Relay fallback can carry video through the vendor's cloud. Microphone/audio,
recording, and driving controls are not provided. The repository documents the
verified model and private dependency APIs; other models are not universally tested.
