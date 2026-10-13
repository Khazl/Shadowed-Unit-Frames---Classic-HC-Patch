# SUF Classic Compatibility

A standalone compatibility addon for World of Warcraft Classic Era and Hardcore. Requires the original Shadowed Unit Frames addon, installed separately from its official distribution.

## What it fixes

Supplies the missing legacy DebuffTypeColor global used by SUF's aura borders, debuff health coloring, and debuff highlights. This addresses the nil-table error reported at auras.lua:562, including enemy Enrage buffs with no dispel type.

An existing table is left unchanged. The addon runs once when loaded, before SUF's login initialization. It has no polling, combat hooks, bundled libraries, or saved settings. It does not modify original addon files and does not address unrelated API errors.

## Install

1. Install the original Shadowed Unit Frames separately.
2. Extract the release ZIP into World of Warcraft/_classic_era_/Interface/AddOns/.
3. Confirm that SUF_ClassicCompatibility/SUF_ClassicCompatibility.toc exists directly under AddOns.
4. Enable Shadowed Unit Frames and SUF Classic Compatibility, then restart the game.
5. Use /sufcompat to check whether the fallback was applied.

For an independent in-game test, use an unmodified original SUF installation. If SUF already contains a color-table fix, /sufcompat will report that an existing table was preserved. Do not delete your WTF folder or SUF saved settings.

Disable this companion addon and reload to stop applying its fallback. A future SUF/client update may make the companion unnecessary.

## Distribution

The upload ZIP contains only the SUF_ClassicCompatibility folder with this addon's own files. No original SUF code, libraries, textures, fonts, or translations are included. Shadowed Unit Frames is a separate required dependency; this project is not affiliated with its authors.

This companion's code is MIT licensed; that license does not apply to Shadowed Unit Frames. This companion uses CurseForge project ID **1742980**. The release ZIP preserves this ID. When listing it on CurseForge, declare Shadowed Unit Frames as a required dependency and select Classic Era game versions. Platform approval remains subject to CurseForge review.

Version 1.0.0. Target: the reported missing-color-table problem in SUF v4.3.9-classic. The user confirmed the standalone addon works in-game.

## GitHub releases

This repository now distributes only the standalone companion. Earlier history and releases may contain the former full-addon version; those are not companion packages.

Publish a release with a new tag targeting the latest main commit. The workflow attaches SUF_ClassicCompatibility-<tag>.zip after validation. Upload that named asset directly to CurseForge, not Source code (zip) or the Actions artifact wrapper. Its sole root folder is SUF_ClassicCompatibility.

To build locally: python scripts/package.py --version 1.0.1