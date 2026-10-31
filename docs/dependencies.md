# Dependencies and project combinations

| Project | Install/configure first | What this project adds |
| --- | --- | --- |
| SunSpec Bridge | `hilman2/ha-sunspec2`, inverter connection | A local Modbus TCP SunSpec endpoint for FEMS/OpenEMS |
| Dreame Live Camera | `Tasshack/dreame-vacuum`, compatible camera and PIN | A native camera entity and session Start/Stop buttons |
| Philips Avent | Compatible monitor and account provisioning; matching bridge app | Monitor controls, sensor/event entities, and video through the chosen bridge |
| Bunker Codex | An existing authenticated HTTPS bridge with the documented API | An Assist conversation agent; HA speech services remain separately configured |
| Dahoam Vacuum Card | A configured Dreame/Valetudo-compatible vacuum and chosen entities | Dashboard controls; optional Dreame Live Camera integration adds the live-view badge |
| Motion Tracker Card | HA motion/presence entities or timestamp/event helpers | A configurable floor-plan history view |
| MeinVodafone | Supported Vodafone Germany account | Usage, plan, and billing sensors; see upstream limitations |
| Shinobi | Shinobi server, API/group keys and MJPEG streams | Legacy camera platform; current HA compatibility unverified |

## Energy path

```text
Physical inverter ← SunSpec2 poller → SunSpec Bridge ← FEMS/OpenEMS
```

SunSpec2 retains the physical inverter connection. FEMS reads the bridge's cached
registers, so faster FEMS requests do not increase the physical polling rate.
Configure polling in SunSpec2 and keep that integration pointed directly at the
inverter rather than back at the bridge.

## Vacuum path

```text
Vacuum integration → cleaning/map entities → Dahoam Vacuum Card
Existing Dreame cloud transport → Dreame Live Camera → optional live-view badge
```

Dreame Live Camera is not a replacement for the vacuum integration. It needs cloud
setup/control even when video travels directly over the LAN; relay fallback may
carry video through the vendor cloud. The card can also use appropriate Valetudo
entities without installing Dreame Live Camera.

## Assistant path

```text
Assist / speech services → Bunker Codex integration → existing HTTPS bridge → Codex
```

The integration does not install Codex or supply a bridge server. Read the bridge
protocol and authorization behavior in its source repository before configuring it.
