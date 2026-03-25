#!/usr/bin/env python3
"""
Build a manifest.json for the TZP client modpack distribution.

Scans mods/ and config/ directories, computes SHA256 hashes and file sizes,
and writes a manifest.json used by the launcher for syncing.

Usage:
    python3 build_manifest.py
"""

import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

PACK_DIR = Path(__file__).resolve().parent
PACK_JSON = PACK_DIR / "pack.json"
MANIFEST_OUT = PACK_DIR / "manifest.json"

# Base URL for file downloads — override via CLI arg for local testing
DEFAULT_BASE_URL = "https://raw.githubusercontent.com/TheZackPack/TZP-client/main"


def tracked_paths(base: Path, *roots: str) -> set[str]:
    """Return Git-tracked file paths under the requested roots."""
    try:
        output = subprocess.run(
            ["git", "ls-files", *roots],
            cwd=base,
            check=True,
            capture_output=True,
            text=True,
        ).stdout
    except (OSError, subprocess.CalledProcessError):
        return set()

    return {line.strip() for line in output.splitlines() if line.strip()}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return f"sha256:{h.hexdigest()}"


def scan_directory(base: Path, subdir: str) -> list[dict]:
    """Walk a subdirectory and return file entries with path, hash, and size."""
    target = base / subdir
    if not target.is_dir():
        return []
    tracked = tracked_paths(base, subdir)
    entries = []
    for root, _dirs, files in os.walk(target):
        for name in sorted(files):
            filepath = Path(root) / name
            rel = filepath.relative_to(base).as_posix()
            if tracked and rel not in tracked:
                continue
            entries.append({
                "path": rel,
                "hash": sha256_file(filepath),
                "size": filepath.stat().st_size,
            })
    return sorted(entries, key=lambda e: e["path"])


def human_size(nbytes: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if nbytes < 1024:
            return f"{nbytes:.1f} {unit}"
        nbytes /= 1024
    return f"{nbytes:.1f} TB"


def main() -> None:
    base_url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_BASE_URL

    if not PACK_JSON.exists():
        print(f"Error: {PACK_JSON} not found.", file=sys.stderr)
        sys.exit(1)

    with open(PACK_JSON) as f:
        pack = json.load(f)

    # Scan mods
    mod_entries = scan_directory(PACK_DIR, "mods")
    for entry in mod_entries:
        entry["required"] = True
        entry["url"] = f"{base_url}/{entry['path']}"

    # Scan configs
    config_entries = scan_directory(PACK_DIR, "config")
    for entry in config_entries:
        entry["url"] = f"{base_url}/{entry['path']}"

    # Scan kubejs
    kubejs_entries = scan_directory(PACK_DIR, "kubejs")
    for entry in kubejs_entries:
        entry["url"] = f"{base_url}/{entry['path']}"

    manifest = {
        "version": pack["version"],
        "minecraft": pack["minecraft"],
        "neoforge": pack["neoforge"],
        "generated": datetime.now(timezone.utc).isoformat(),
        "files": mod_entries,
        "configs": config_entries,
        "kubejs": kubejs_entries,
    }

    with open(MANIFEST_OUT, "w") as f:
        json.dump(manifest, f, indent=2)
        f.write("\n")

    total_files = len(mod_entries) + len(config_entries) + len(kubejs_entries)
    total_size = sum(e["size"] for e in mod_entries + config_entries + kubejs_entries)

    print(f"TZP Manifest v{pack['version']} built successfully")
    print(f"  Mods:    {len(mod_entries)} files")
    print(f"  Configs: {len(config_entries)} files")
    print(f"  KubeJS:  {len(kubejs_entries)} files")
    print(f"  Total:   {total_files} files ({human_size(total_size)})")
    print(f"  Output:  {MANIFEST_OUT}")


if __name__ == "__main__":
    main()
