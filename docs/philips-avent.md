# Philips Avent Baby Monitor

[Source and full guide](https://github.com/felixsteghofer/aventproxy) ·
[LAN bridge setup](https://github.com/felixsteghofer/aventproxy/blob/main/aventproxy-lan-addon/DOCS.md) ·
[Issues](https://github.com/felixsteghofer/aventproxy/issues)

This fork provides Philips Avent/Tuya baby-monitor entities and a LAN-only operating
option. Domain: `philips_avent`. Available features include video, temperature,
night light, lullabies, privacy, and sound/motion events, depending on the model.
The repository also contains separately installed bridge apps.

## Setup

1. Add `felixsteghofer/aventproxy` to HACS as **Integration**, download it and restart HA.
2. Add the same repository under **Settings → Apps → App store → Repositories**
   for the required bridge app. Follow the project guide to choose the original
   cloud-assisted bridge or the LAN bridge; keep companion versions compatible.
3. Add **Philips Avent Baby Monitor** under Devices & services. Provision the account
   through the integration's UI, including the correct region and verification code.
4. Follow the LAN guide when choosing local operation. Configure bridge location
   through the integration rather than assuming an external bridge is on localhost.

[Add the app repository](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Ffelixsteghofer%2Faventproxy).

Local operation still requires the documented initial provisioning. Model-specific
support and event behavior vary; consult the supported-device table and diagnostics
guide. HACS manages the integration, while Supervisor manages the bridge app.
