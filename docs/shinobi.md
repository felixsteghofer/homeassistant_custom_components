# Shinobi — legacy integration

[Retained source](../custom_components/shinobi) ·
[Preserved original documentation](shinobi-original.md) ·
[Shinobi API documentation](https://shinobi.video/docs/api)

The original project in this repository connects Shinobi CCTV monitors to a
Home Assistant camera platform. Its code remains unchanged by the catalogue
conversion. It uses YAML configuration and MJPEG streams rather than the modern
UI-configured packaging used by the newer integrations.

## Compatibility and original setup

The preserved guide was written for older Home Assistant releases; compatibility
with current HA is **unverified**. Do not treat it as a current HACS installation
recommendation. Review/update and test the component before deploying it on a
modern instance.

Historically, installation copied `custom_components/shinobi` into HA's config
folder and configured the Shinobi server, API/group keys and the camera platform.
Active Record/Watch-only monitors were exposed as MJPEG cameras; optional name-based
allow/deny filters selected monitors. The preserved guide contains the original
configuration example and known feature requests.

Shinobi must expose the expected API and MJPEG streams. Credentials belong in
private Home Assistant configuration, never in this catalogue. The original guide
is retained for context; it is not a declaration that its APIs still match current HA.
