# Maintaining the catalogue

## Add or change a project

1. Add/update an entry in [repositories.json](../repositories.json).
2. Create/update its page under `docs/`. Explain its purpose, installation type,
   setup dependencies, configuration entry/card type, and material limitations.
   Link to its source README and issue tracker for complete, current instructions.
3. Run `python3 scripts/catalog.py --write` to regenerate the README overview.
4. Run `python3 scripts/catalog.py --check` and `git diff --check`.
5. Review and commit the manifest, documentation, and generated table together.

GitHub Actions repeats the offline consistency check on pushes and pull requests.
The checker verifies categories, required fields, duplicate IDs/repositories, local
Markdown links, project pages, HACS source identifiers and the generated overview.
It does not install integrations, contact Home Assistant, or prove remote device
compatibility. External links are reviewed separately when catalogue entries change.

## Manifest

`schema_version` is currently `1`; `projects` is an ordered list. Each entry has:

- `id`, `name`, `repository` (`owner/repo`), `kind`, `summary`, `requires`, and
  `documentation` (a repository-relative Markdown path).
- `domain` for an integration/reference/legacy entry, or `card_type` for a card.
- `hacs_repository` for an installable project. `integration` and `reference`
  entries use the `integration` redirect category; dashboard entries use `plugin`.
- Optional `upstream_repository` to distinguish a personal fork from its upstream
  source, and `app_repository` for the separately managed Avent bridge apps.
- `source_path` for the legacy code retained inside this central repository.

The MeinVodafone entry intentionally has different `repository` and
`hacs_repository` values: its personal fork is included, while the installation
link preserves the upstream choice. Do not silently change HACS sources to forks.

## Repository ownership and releases

Make code changes, tests, tags, and releases in each project's own repository.
Shared catalogue changes do not bump those projects' versions. Keep existing
integration domains and identifiers stable during ordinary updates.

The central repository retains Shinobi's original implementation and documentation.
Do not mark it compatible with a current Home Assistant version without testing
and updating its own code/package metadata. The old source is not a template for
modern config-flow integrations.

No submodules are needed to browse or maintain this catalogue. If a developer wants
several checkouts, clone the relevant repositories side by side. Credentials,
connection files, live deployment data, and real floor plans belong outside the
public catalogue.
