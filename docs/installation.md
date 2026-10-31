# Installation and updates

## What the central repository provides

This is an index and documentation hub. HACS custom repositories are registered
individually; this JSON catalogue and Git submodules are not a native HACS
collection/import mechanism. Register the project's actual repository using its
**Add to HACS** link from the overview. You can register only the projects you need.

## Integrations

In HACS, open **⋮ → Custom repositories**, add the linked GitHub URL with category
**Integration**, and download the integration. Restart Home Assistant, then use
**Settings → Devices & services → Add integration**. Its project guide describes
connection settings and any additional dependencies.

For existing manual installations, follow the project's migration instructions.
Preserving a domain and its existing config entry can preserve entity IDs and
settings; deleting and recreating that entry is not a general update procedure.
Adding the central catalogue alone does not change any existing HACS installation.

## Dashboard cards

Add the card's repository with category **Dashboard** and download it. HACS may
show this type internally as `plugin` or `lovelace`; this catalogue uses `dashboard`
for its human-readable project type. HACS links use the redirect category `plugin`.

Refresh the browser after downloading. Check **Settings → Dashboards → Resources**
if the card is not available, and follow the project's JavaScript module-resource
instructions. Configure the card using existing entities in the dashboard editor.
Downloading a card does not create or configure its backend integrations.

## Philips Avent bridge apps

The Avent repository also contains Home Assistant OS apps. Add that repository
separately under **Settings → Apps → App store → ⋮ → Repositories**. Select the
bridge matching the integration's operating mode and version. HACS installs the
integration, while Supervisor manages the app. Follow the Avent guide when moving
between its original cloud-assisted and LAN-only modes.

## Updates and forks

Use HACS's update UI for the individual integration or card, read release notes,
and restart/refresh when requested. Manage companion apps and external bridge
services through their own update paths.

The MeinVodafone entry links the personal fork for reference and the upstream
repository for installation. The inventoried HA installation uses upstream. Do not
install both copies of the same integration domain: compare changes/releases and
follow a deliberate migration if you decide to switch.

## Verification

After an integration change, run Home Assistant's built-in **Tools → YAML → Check
configuration** (or `ha core check`). Check the integration's loaded state and real
readings/actions relevant to the change. For a dashboard card, confirm its resource
loads and its configured entities resolve. A catalogue/documentation-only update
does not require a Home Assistant restart or configuration change.

References: [HACS integration layout](https://www.hacs.xyz/docs/publish/integration/),
[HACS custom repositories](https://www.hacs.dev/docs/faq/custom_repositories/).
