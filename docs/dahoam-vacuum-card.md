# Dahoam Vacuum Card

[Source and full guide](https://github.com/felixsteghofer/home-assistant_custom-vacuum-card) ·
[Examples](https://github.com/felixsteghofer/home-assistant_custom-vacuum-card/tree/main/examples) ·
[Issues](https://github.com/felixsteghofer/home-assistant_custom-vacuum-card/issues)

A compact dashboard card for vacuum state, map preview, room cleaning, cleaning
settings, station controls, and maintenance. It uses existing HA entities and
services; supported controls depend on the selected vacuum integration.

## Setup

1. Configure the vacuum and its relevant entities first.
2. Add `felixsteghofer/home-assistant_custom-vacuum-card` to HACS as **Dashboard**
   and download it. Refresh the frontend; check dashboard resources if necessary.
3. Add **Dahoam Vacuum** in the dashboard editor. The general type is
   `custom:dahoam-vacuum-card`; `custom:dahoam-dreame-card` remains a compatibility alias.
4. Select the vacuum and explicitly configure optional map, station, mode, water,
   and sensor entities in the visual editor.

The resource file is `dahoam-dreame-card.js`; the source README also documents manual
resource installation. An optional `live_camera_entity` adds the camera badge;
Dreame Live Camera can provide that entity. Keep its PIN in integration options.

Dreame room cleaning and suitable Valetudo entity controls are supported; Valetudo
room/zone commands are not implemented in the documented release. A map preview is
not map editing. Capability filtering hides unsupported controls; the card does
not configure or flash devices. Consult the upstream guide for current limitations.
