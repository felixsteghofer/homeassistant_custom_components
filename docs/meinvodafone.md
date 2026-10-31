# MeinVodafone fork and upstream installation

[Personal fork](https://github.com/felixsteghofer/homeassistant-meinvodafone) ·
[Upstream source and guide](https://github.com/stickpin/homeassistant-meinvodafone) ·
[Upstream issues](https://github.com/stickpin/homeassistant-meinvodafone/issues)

Monitors Vodafone Germany contract usage, including minutes, SMS, data, plans and
billing information. Domain: `meinvodafone`.

The personal fork is included as a related repository. The inventoried Home
Assistant installation uses **stickpin/homeassistant-meinvodafone**, so this
catalogue's installation link intentionally points upstream. Listing the fork is
not a recommendation to switch a working installation to it.

## Setup

1. Add `stickpin/homeassistant-meinvodafone` to HACS as **Integration** and download it.
2. Restart Home Assistant and add **MeinVodafone** under Devices & services.
3. Follow the current upstream UI to authenticate and select the intended contract.
4. Verify the expected usage and billing entities against the account portal.

Check current upstream authentication support and refresh limits before configuring
accounts. Do not repeatedly retry account authentication without consulting its
guidance. Keep account details and contract identifiers out of public documentation.

If you need a fork-specific change, compare the fork's changes, compatibility and
published releases first. Plan a source migration for the existing domain; do not
install two copies of `meinvodafone` under different repositories simultaneously.
