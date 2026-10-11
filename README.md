# Shadowed Unit Frames - Classic Reborn

Community-maintained Classic compatibility fixes based on Shadowed Unit Frames v4.3.9-classic by Shadowed and contributors.

Original project: https://github.com/Nevcairiel/ShadowedUnitFrames

## Current fix

Restores the legacy `DebuffTypeColor` table when the client does not provide it. This fixes the nil-table lookup at `modules/auras.lua:562`, including enemy Enrage buffs, and supplies the same colors to the health bar and debuff highlight modules. An existing color table is preserved.

The compatibility block is in `ShadowedUnitFrames.lua`, before the affected modules load. This snapshot was taken from a Classic Era / Hardcore installation. File changes were verified; in-game validation is still pending. This is not a claim that every client compatibility issue is fixed.

## Installation

1. Download this repository and extract it.
2. Rename the extracted repository folder to `ShadowedUnitFrames` and put it in `World of Warcraft/_classic_era_/Interface/AddOns/`.
3. Copy the included `options` folder to the same `AddOns` directory and rename that copy to `ShadowedUF_Options`.
4. Enable both addons. Restart the game after installing, or use `/reload` when safely out of combat after updating an existing installation.

The main `.toc` file must be directly inside `AddOns/ShadowedUnitFrames/`; the options `.toc` must be directly inside `AddOns/ShadowedUF_Options/`.

Back up an existing installation before replacing it. Existing SUF profiles use the unchanged `ShadowedUFDB` saved variable. Addon managers may overwrite this compatibility fix when installing an upstream update.

## Repository contents

The main addon is at the repository root. `options/` contains the companion configuration addon, with its bundled libraries. Local backup files are excluded from version control.

Original author attribution and bundled library notices are retained. This repository does not relicense the original addon or its dependencies.
