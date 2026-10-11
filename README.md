# Shadowed Unit Frames - Classic Reborn

Community-maintained Classic compatibility fixes based on Shadowed Unit Frames v4.3.9-classic by Shadowed and contributors.

Original project: https://github.com/Nevcairiel/ShadowedUnitFrames

## Current fix

Restores the legacy `DebuffTypeColor` table when the client does not provide it. This fixes the nil-table lookup at `modules/auras.lua:562`, including enemy Enrage buffs, and supplies the same colors to the health bar and debuff highlight modules. An existing color table is preserved.

The compatibility block is in `ShadowedUnitFrames.lua`, before the affected modules load. This snapshot was taken from a Classic Era / Hardcore installation. File changes were verified; in-game validation is still pending. This is not a claim that every client compatibility issue is fixed.

## Installation

1. Download the named `ShadowedUnitFrames-Classic-Reborn-<version>.zip` asset from GitHub Releases (not Source code) and extract both addon folders into `World of Warcraft/_classic_era_/Interface/AddOns/`.
2. Confirm that `ShadowedUnitFrames` and `ShadowedUF_Options` are sibling folders directly inside `AddOns`.
3. For a source checkout instead, install the repository as `ShadowedUnitFrames` and copy `options/` beside it as `ShadowedUF_Options`.
4. Enable both addons. Restart the game after installing, or use `/reload` when safely out of combat after updating an existing installation.

The main `.toc` file must be directly inside `AddOns/ShadowedUnitFrames/`; the options `.toc` must be directly inside `AddOns/ShadowedUF_Options/`.

Back up an existing installation before replacing it. Existing SUF profiles use the unchanged `ShadowedUFDB` saved variable. Addon managers may overwrite this compatibility fix when installing an upstream update.

## Repository contents

The main addon is at the repository root. `options/` contains the companion configuration addon, with its bundled libraries. Local backup files are excluded from version control.

Original author attribution and bundled library notices are retained. This repository does not relicense the original addon or its dependencies.

## Publishing a release for CurseForge

1. On GitHub, create a release with a new tag targeting the latest commit on `main`, including the packaging workflow. Use a filename-safe tag such as `v4.3.9-reborn.1`.
2. Click **Publish release**. The **Package addon** workflow builds and checks the ZIP, then attaches it to that release. Wait for the workflow to finish.
3. Under release Assets, download `ShadowedUnitFrames-Classic-Reborn-<tag>.zip`. Do not upload GitHub's automatic **Source code (zip)** archive to CurseForge.
4. Upload that named ZIP to your own CurseForge project and select the appropriate supported Classic game versions. No automatic CurseForge upload or API key is configured.

The archive has exactly two top-level folders: `ShadowedUnitFrames/` and `ShadowedUF_Options/`. Both TOCs receive the release tag as their version. Bundled libraries are included; Git files, workflows, build scripts, backups, and build output are excluded. The main addon identifies CurseForge project **1739222**; the release packager preserves this ID. The original WoWInterface project ID remains excluded.

Publishing a release from an older commit without the workflow will not package it. Merely saving a draft does not trigger packaging. Pushes and manual Actions runs also build a preview ZIP without publishing a release. For local packaging, run `python scripts/package.py --version v4.3.9-reborn.1`; the ZIP is written to `dist/`.