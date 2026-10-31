# Motion Tracker Card

[Source and full guide](https://github.com/felixsteghofer/home-assistant_motion-tracker-card) ·
[Fictional example](https://github.com/felixsteghofer/home-assistant_motion-tracker-card/blob/main/examples/basic.json) ·
[Issues](https://github.com/felixsteghofer/home-assistant_motion-tracker-card/issues)

Shows recent detections on configurable vector floor plans, including separate
latest/fresh/recent colors, expiry, room selection, and recorder-backed history.
Multiple detectors can report to the same room.

## Setup

1. Add `felixsteghofer/home-assistant_motion-tracker-card` to HACS as **Dashboard**,
   download it, refresh the browser, and verify its module resource.
2. Add a card of type `custom:motion-tracker-card` in the dashboard editor.
3. Start from the source repository's fictional example. Define floor geometry,
   room IDs and your existing motion/presence entities or timestamp/event helpers.
4. Use the visual editor or full configuration editor to tune mappings, colors,
   history window, and refresh behavior.

If HACS does not register the resource, use the JavaScript module URL
`/hacsfiles/home-assistant_motion-tracker-card/motion-tracker-card.js`.

The card reads configured entities and history; it does not create motion sensors
or operate devices. Recorder retention/exclusions limit available history. A sensor
remaining on cannot describe every subsequent movement, and missing events do not
prove no motion. Use offset-bearing ISO timestamps for persistent event data. Keep
real floor plans and household mappings in private dashboard configuration.
