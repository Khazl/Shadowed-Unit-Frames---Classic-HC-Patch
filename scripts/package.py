"""Build and validate an installable WoW addon ZIP using only tracked files."""
import argparse
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
MAIN = "ShadowedUnitFrames"
OPTIONS = "ShadowedUF_Options"


def build(version):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,99}", version):
        raise ValueError("Version must be 1-100 filename-safe characters (letters, digits, dots, underscores, hyphens).")
    tracked = subprocess.check_output(
        ["git", "ls-files", "-z"], cwd=ROOT
    ).decode("utf-8").split("\0")
    payload = {}
    root_files = {"ShadowedUnitFrames.lua", "ShadowedUnitFrames.toc",
                  "ShadowedUnitFrames.xml", "ExternalAPI.lua", "CHANGELOG.md", "README.md"}
    for name in filter(None, tracked):
        path = PurePosixPath(name)
        if path.parts[0] == "options":
            dest = str(PurePosixPath(OPTIONS, *path.parts[1:]))
        elif path.parts[0] in {"libs", "localization", "media", "modules"} or name in root_files or path.name.lower().startswith(("license", "copying", "notice")):
            dest = str(PurePosixPath(MAIN, path))
        else:
            continue
        if any(part.startswith(".") for part in path.parts) or re.search(r"\.(bak|orig|rej)(\.|$)", name):
            continue
        data = (ROOT / name).read_bytes()
        if dest in {f"{MAIN}/{MAIN}.toc", f"{OPTIONS}/{OPTIONS}.toc"}:
            text = data.decode("utf-8-sig")
            text = re.sub(r"^## X-(?:Curse-Project-ID|WoWI-ID):.*\n?", "", text, flags=re.M)
            text = re.sub(r"^## Version:.*$", f"## Version: {version}", text, flags=re.M)
            if not re.search(r"^## Version:", text, re.M):
                text = f"## Version: {version}\n" + text
            data = text.encode("utf-8")
        payload[dest] = data
    for folder in (MAIN, OPTIONS):
        toc = f"{folder}/{folder}.toc"
        if toc not in payload:
            raise ValueError(f"Missing addon manifest: {toc}")
        for line in payload[toc].decode("utf-8-sig").splitlines():
            entry = line.split(" [AllowLoadGameType", 1)[0].strip()
            if entry and not entry.startswith("#"):
                target = f"{folder}/" + entry.replace("\\", "/")
                if target not in payload:
                    raise ValueError(f"Manifest references missing file: {target}")
    output = ROOT / "dist" / f"ShadowedUnitFrames-Classic-Reborn-{version}.zip"
    output.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(payload.items()):
            archive.writestr(name, data)
    with zipfile.ZipFile(output) as archive:
        assert archive.testzip() is None, "ZIP integrity check failed"
        assert {name.split("/")[0] for name in archive.namelist()} == {MAIN, OPTIONS}
        assert all(archive.read(name) == data for name, data in payload.items())
    print(f"Validated {len(payload)} files in {output}")
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as stream:
            stream.write(f"zip_path={output.relative_to(ROOT).as_posix()}\n")
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", required=True)
    build(parser.parse_args().version)
