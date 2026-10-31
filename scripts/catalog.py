#!/usr/bin/env python3
"""Validate the project index and generate the README overview; no HA writes."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlencode, urlsplit

ROOT = Path(__file__).resolve().parents[1]
KINDS = {
    "integration": "Integration",
    "dashboard": "Dashboard",
    "reference": "Fork / reference",
    "legacy": "Legacy integration",
}
REPOSITORY = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+")
START, END = "<!-- catalog:start -->", "<!-- catalog:end -->"


def load_projects():
    data = json.loads((ROOT / "repositories.json").read_text())
    if data.get("schema_version") != 1:
        raise ValueError("Unsupported catalogue schema_version")
    projects = data["projects"]
    if not isinstance(projects, list) or not projects:
        raise ValueError("projects must be a non-empty list")
    ids, repositories = set(), set()
    for project in projects:
        for key in (
            "id",
            "name",
            "repository",
            "kind",
            "summary",
            "requires",
            "documentation",
        ):
            if not isinstance(project.get(key), str) or not project[key].strip():
                raise ValueError(f"Project requires a non-empty {key}")
        if project["kind"] not in KINDS:
            raise ValueError(f"Unknown project kind: {project['kind']}")
        if not re.fullmatch(r"[a-z0-9-]+", project["id"]):
            raise ValueError(f"Invalid project id: {project['id']}")
        for key in (
            "repository",
            "hacs_repository",
            "upstream_repository",
            "app_repository",
        ):
            if key in project and not REPOSITORY.fullmatch(project[key]):
                raise ValueError(f"Invalid {key}: {project[key]}")
        if project["id"] in ids or project["repository"].lower() in repositories:
            raise ValueError(f"Duplicate project: {project['id']}")
        ids.add(project["id"])
        repositories.add(project["repository"].lower())
        page = (ROOT / project["documentation"]).resolve()
        if not page.is_relative_to(ROOT) or not page.is_file() or page.suffix != ".md":
            raise ValueError(
                f"Missing/invalid project page: {project['documentation']}"
            )
        if project["kind"] == "dashboard":
            if not project.get("card_type", "").startswith("custom:"):
                raise ValueError(f"Dashboard requires card_type: {project['id']}")
        elif not re.fullmatch(r"[a-z][a-z0-9_]*", project.get("domain", "")):
            raise ValueError(f"Project requires domain: {project['id']}")
        if project["kind"] in ("integration", "dashboard", "reference"):
            if not project.get("hacs_repository"):
                raise ValueError(f"Missing HACS source: {project['id']}")
        elif project.get("hacs_repository"):
            raise ValueError("Legacy entries must not advertise a HACS install")
        if project.get("source_path") and not (ROOT / project["source_path"]).is_dir():
            raise ValueError(f"Missing source directory: {project['source_path']}")
    return projects


def hacs_url(project):
    owner, repository = project["hacs_repository"].split("/")
    category = "plugin" if project["kind"] == "dashboard" else "integration"
    return "https://my.home-assistant.io/redirect/hacs_repository/?" + urlencode(
        {
            "owner": owner,
            "repository": repository,
            "category": category,
        }
    )


def overview(projects):
    lines = [
        "| Project | Type | Purpose | Installation | Documentation |",
        "| --- | --- | --- | --- | --- |",
    ]
    for project in projects:
        installation = "Manual legacy setup"
        if project.get("hacs_repository"):
            label = (
                "Add upstream to HACS"
                if project["hacs_repository"] != project["repository"]
                else "Add to HACS"
            )
            installation = f"[{label}]({hacs_url(project)})"
        lines.append(
            f"| [{project['name']}](https://github.com/{project['repository']}) "
            f"| {KINDS[project['kind']]} | {project['summary']} "
            f"| {installation} | [Setup]({project['documentation']}) |"
        )
    return "\n".join(lines)


def generated_readme(projects):
    text = (ROOT / "README.md").read_text()
    if text.count(START) != 1 or text.count(END) != 1:
        raise ValueError("README requires exactly one catalogue marker pair")
    before, rest = text.split(START)
    previous, after = rest.split(END)
    return before + START + "\n\n" + overview(projects) + "\n\n" + END + after


def check_local_links():
    for page in [ROOT / "README.md", *(ROOT / "docs").glob("*.md")]:
        for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", page.read_text()):
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            destination = (page.parent / parts.path).resolve()
            if not destination.is_relative_to(ROOT) or not destination.exists():
                raise ValueError(
                    f"Broken local link in {page.relative_to(ROOT)}: {target}"
                )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--check", action="store_true", help="Validate catalogue and generated README"
    )
    mode.add_argument(
        "--write", action="store_true", help="Update the README overview from JSON"
    )
    mode.add_argument(
        "--list", action="store_true", help="Print the catalogued repositories"
    )
    args = parser.parse_args()
    try:
        projects = load_projects()
        expected = generated_readme(projects)
        if args.write:
            (ROOT / "README.md").write_text(expected)
        if args.check and (ROOT / "README.md").read_text() != expected:
            raise ValueError(
                "README overview is stale; run python3 scripts/catalog.py --write"
            )
        check_local_links()
        if args.list:
            for project in projects:
                print(
                    f"{project['kind']:12} {project['repository']} ({project['name']})"
                )
        else:
            print(
                f"Catalogue valid: {len(projects)} projects; local documentation links checked."
            )
    except (KeyError, ValueError, OSError) as error:
        parser.exit(1, f"Catalogue error: {error}\n")


if __name__ == "__main__":
    main()
