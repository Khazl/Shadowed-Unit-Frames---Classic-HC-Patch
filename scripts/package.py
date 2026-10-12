"""Package only the standalone companion addon, never the original SUF."""
import argparse
import os
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ADDON = "SUF_ClassicCompatibility"
FILES = (ADDON + ".toc", "Compatibility.lua", "LICENSE", "README.md")


def build(version):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,99}", version):
        raise ValueError("Use a filename-safe release tag, e.g. 1.0.1")
    payload = {f"{ADDON}/{name}": (ROOT / name).read_bytes() for name in FILES}
    toc_name = f"{ADDON}/{ADDON}.toc"
    toc = payload[toc_name].decode("utf-8-sig")
    toc, count = re.subn(r"(?m)^## Version:[^\r\n]*", f"## Version: {version}", toc)
    if count != 1 or "## Dependencies: ShadowedUnitFrames" not in toc:
        raise ValueError("Invalid companion addon metadata")
    for line in toc.splitlines():
        entry = line.strip()
        if entry and not entry.startswith("#") and f"{ADDON}/{entry}" not in payload:
            raise ValueError(f"Missing manifest file: {entry}")
    payload[toc_name] = toc.encode("utf-8")
    output = ROOT / "dist" / f"{ADDON}-{version}.zip"
    output.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(f"{ADDON}/", b"")
        for name, data in sorted(payload.items()):
            archive.writestr(name, data)
    with zipfile.ZipFile(output) as archive:
        assert archive.testzip() is None
        assert set(archive.namelist()) == {f"{ADDON}/", *payload}
        assert all(archive.read(name) == data for name, data in payload.items())
    print(f"Verified standalone addon ZIP: {output}")
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as stream:
            stream.write(f"zip_path={output.relative_to(ROOT).as_posix()}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", required=True)
    build(parser.parse_args().version)
