# Bunker Codex

[Source and full guide](https://github.com/felixsteghofer/home-assistant_custom-assistant) ·
[Bridge protocol](https://github.com/felixsteghofer/home-assistant_custom-assistant/blob/main/docs/bridge-protocol.md) ·
[Issues](https://github.com/felixsteghofer/home-assistant_custom-assistant/issues)

Connects an existing compatible Codex HTTPS bridge to Home Assistant as an Assist
conversation agent. Domain: `bunker_codex`. Supports follow-up conversations and
can handle recognized simple requests through HA's built-in agent first.

## Setup

1. Have a compatible authenticated HTTPS bridge running on the Codex host. It must
   implement the documented health/conversation API; a raw app-server endpoint is
   not that bridge. Manage Codex login and workspace tools on that host.
2. Add `felixsteghofer/home-assistant_custom-assistant` to HACS as **Integration**,
   download it, restart HA, and add **Bunker Codex** under Devices & services.
3. Enter the bridge HTTPS URL, bridge access token, and CA certificate when needed.
   Certificate and hostname validation remain required.
4. Select Bunker Codex as the conversation agent under **Settings → Voice assistants**.
   Configure your existing speech-to-text/text-to-speech services separately.

This package does not install Codex, deploy the bridge, or copy authentication files.
Administrator users are allowed by default; enabling access for voice devices without
an HA user deliberately broadens access to the personal agent. Read the source guide's
authorization and approval behavior before changing that option.
