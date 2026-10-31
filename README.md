# Home Assistant custom components

A central catalogue of the Home Assistant integrations, dashboard cards, and
related forks maintained under **felixsteghofer**. Start here to find a project,
understand its dependencies, and open its repository in HACS.

Each project keeps its own source repository, releases, issue tracker, and update
history. Adding this catalogue to HACS does **not** register the other repositories;
use the individual links below. HACS manages one integration per repository.
See [installation](docs/installation.md) and the
[HACS repository requirements](https://www.hacs.xyz/docs/publish/integration/).

## Project overview

<!-- catalog:start -->

| Project | Type | Purpose | Installation | Documentation |
| --- | --- | --- | --- | --- |
| [SunSpec Bridge](https://github.com/felixsteghofer/homeassistant_sunspec-bridge) | Integration | Serve existing SunSpec2 inverter readings to FEMS/OpenEMS over Modbus TCP. | [Add to HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=felixsteghofer&repository=homeassistant_sunspec-bridge&category=integration) | [Setup](docs/sunspec-bridge.md) |
| [Dreame Live Camera](https://github.com/felixsteghofer/dreame-live-camera) | Integration | PIN-gated live video from compatible Dreame/MOVA robot vacuums. | [Add to HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=felixsteghofer&repository=dreame-live-camera&category=integration) | [Setup](docs/dreame-live-camera.md) |
| [Philips Avent Baby Monitor](https://github.com/felixsteghofer/aventproxy) | Integration | Baby-monitor video, temperature, night light, lullabies and alerts; includes LAN bridge apps. | [Add to HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=felixsteghofer&repository=aventproxy&category=integration) | [Setup](docs/philips-avent.md) |
| [Bunker Codex](https://github.com/felixsteghofer/home-assistant_custom-assistant) | Integration | Use an existing Codex HTTPS bridge as a native Home Assistant Assist conversation agent. | [Add to HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=felixsteghofer&repository=home-assistant_custom-assistant&category=integration) | [Setup](docs/bunker-codex.md) |
| [Dahoam Vacuum Card](https://github.com/felixsteghofer/home-assistant_custom-vacuum-card) | Dashboard | Vacuum map, cleaning controls, room selection and dock controls in a compact card. | [Add to HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=felixsteghofer&repository=home-assistant_custom-vacuum-card&category=plugin) | [Setup](docs/dahoam-vacuum-card.md) |
| [Motion Tracker Card](https://github.com/felixsteghofer/home-assistant_motion-tracker-card) | Dashboard | Show recent detections on configurable vector floor plans using HA entities and recorder history. | [Add to HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=felixsteghofer&repository=home-assistant_motion-tracker-card&category=plugin) | [Setup](docs/motion-tracker-card.md) |
| [MeinVodafone fork](https://github.com/felixsteghofer/homeassistant-meinvodafone) | Fork / reference | Reference to the personal fork of the Vodafone Germany contract-usage integration. | [Add upstream to HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=stickpin&repository=homeassistant-meinvodafone&category=integration) | [Setup](docs/meinvodafone.md) |
| [Shinobi (legacy)](https://github.com/felixsteghofer/homeassistant_custom_components) | Legacy integration | Original YAML-based Shinobi CCTV camera integration retained in this repository. | Manual legacy setup | [Setup](docs/shinobi.md) |

<!-- catalog:end -->

The catalogue covers the public Home Assistant projects identified on 2026-10-31.
It includes original projects, the Avent and MeinVodafone forks, and this repo's
legacy Shinobi implementation. Upstream dependencies and the Home Assistant Core
fork are not presented as integrations maintained here. A catalogue listing does
not mean a project is installed in your HA instance or tested with every HA version.

## Install a project

1. Choose a project and read its linked setup guide and upstream README.
2. Use **Add to HACS**, or add its repository manually under
   **HACS → ⋮ → Custom repositories**. Select **Integration** or **Dashboard** as
   shown in the overview.
3. Download the project. For integrations, restart Home Assistant and add/configure
   it under **Settings → Devices & services**. For cards, refresh the browser and
   add the card in the dashboard editor.
4. Install each project's required backend or companion integration separately.
   HACS downloading a card does not install its vacuum integration, and downloading
   an integration does not provision its external bridge.

[Detailed installation and updates](docs/installation.md) ·
[Dependencies and combinations](docs/dependencies.md) ·
[Catalogue maintenance](docs/maintaining.md)

## Useful combinations

- **SunSpec2 + SunSpec Bridge → FEMS/OpenEMS:** retain one connection to the physical
  inverter while FEMS reads the bridge's cached SunSpec register map.
- **Dreame Vacuum + Dreame Live Camera + Dahoam Vacuum Card:** use existing cleaning
  entities and optional PIN-gated live video in one dashboard card.
- **Motion/presence entities + Motion Tracker Card:** map detections onto your own
  floor geometry without embedding real floor plans in this repository.
- **Compatible Codex HTTPS bridge + Bunker Codex + HA speech services:** expose the
  existing assistant through Home Assistant Assist.

## Source repositories and development

[repositories.json](repositories.json) is the machine-readable index. It records
project type, repository, domain/card type, dependencies, local documentation, and
HACS source. It is a catalogue manifest, not an import format understood by HACS.
The overview table is generated from that file.

```sh
python3 scripts/catalog.py --list
python3 scripts/catalog.py --write
python3 scripts/catalog.py --check
```

To develop a project, clone its own repository and follow its README. Submodules
are not required for this catalogue; ordinary clones keep development checkouts
and releases independent. See [maintenance](docs/maintaining.md) before adding a
project, changing a HACS source, or updating shared instructions.

## Legacy Shinobi

The original implementation remains at
[custom_components/shinobi](custom_components/shinobi). Its
[setup and compatibility notes](docs/shinobi.md) link to the
[preserved original documentation](docs/shinobi-original.md). Its compatibility
with current Home Assistant releases has not been validated.

## Support

Report device, integration, or card issues in that project's issue tracker; use
[this repository's issues](https://github.com/felixsteghofer/homeassistant_custom_components/issues)
for catalogue errors or missing links. Avoid including tokens, account credentials,
private camera images, real floor plans, or HA storage exports in public reports.
Project licenses and compatibility requirements are defined in each source repository.
