#!/usr/bin/env python3
"""Download the official IPA links in apps.json. Python 3.9+, no packages."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import urllib.error
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parent
HEADERS = {"User-Agent": "Ponze-iPhone-Sideload-Collection/1.0"}


def request(url, method="GET"):
    if not url.startswith("https://"):
        raise ValueError("Only HTTPS downloads are supported")
    return urllib.request.urlopen(
        urllib.request.Request(url, headers=HEADERS, method=method), timeout=45
    )


def file_hash(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate(path, asset):
    if asset.get("size") and path.stat().st_size != asset["size"]:
        raise ValueError("Downloaded size differs from the official metadata")
    digest = file_hash(path)
    if asset.get("sha256") and digest != asset["sha256"]:
        raise ValueError("SHA-256 differs from the hash published upstream")
    with zipfile.ZipFile(path) as archive:
        if not any(name.startswith("Payload/") and ".app/Info.plist" in name
                   for name in archive.namelist()):
            raise ValueError("The download is not an iPhone IPA (missing Payload)")
        bad = archive.testzip()
        if bad:
            raise ValueError("Damaged ZIP member: " + bad)
    return digest


def download(app, output):
    asset = app["download"]
    folder = output / app["id"]
    folder.mkdir(parents=True, exist_ok=True)
    filename = Path(asset["filename"]).name
    target = folder / filename
    if target.exists():
        digest = validate(target, asset)
        print("  Already downloaded and verified: " + str(target))
    else:
        temporary = target.with_suffix(target.suffix + ".part")
        try:
            print("  Downloading " + asset["version"] + " ...", flush=True)
            with request(asset["url"]) as response, temporary.open("wb") as handle:
                length = int(response.headers.get("Content-Length", 0))
                received = 0
                previous = -1
                for chunk in iter(lambda: response.read(1024 * 1024), b""):
                    handle.write(chunk)
                    received += len(chunk)
                    progress = received * 100 // length if length else received // (16 * 1024 * 1024)
                    if progress // 10 != previous:
                        previous = progress // 10
                        print("    %.1f MiB%s" % (received / 1048576,
                              " / %.1f MiB" % (length / 1048576) if length else ""), flush=True)
                if length and received != length:
                    raise ValueError("Incomplete HTTP download")
            digest = validate(temporary, asset)
            temporary.replace(target)
        except BaseException:
            temporary.unlink(missing_ok=True)
            raise
    target.with_suffix(".ipa.sha256").write_text(digest + "  " + filename + "\n", encoding="utf-8")
    print("  Installer: " + app["installer"])
    print("  Note: " + app["notes"])
    return {"id": app["id"], "name": app["name"], "path": str(target.resolve()),
            "source": asset["url"], "version": asset["version"], "sha256": digest}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    choice = parser.add_mutually_exclusive_group()
    choice.add_argument("--all", action="store_true", help="Download all available IPAs")
    choice.add_argument("--app", action="append", metavar="ID", help="Download one app; repeatable")
    choice.add_argument("--check", action="store_true", help="Check download URLs without downloading")
    choice.add_argument("--list", action="store_true", help="List the complete catalog")
    parser.add_argument("--output", type=Path, default=ROOT / "downloads")
    args = parser.parse_args()
    catalog = json.loads((ROOT / "apps.json").read_text(encoding="utf-8"))
    apps = catalog["apps"]
    known = {app["id"] for app in apps}
    unknown = set(args.app or []) - known
    if unknown:
        parser.error("Unknown app IDs: " + ", ".join(sorted(unknown)))
    if not (args.all or args.app or args.check):
        for app in apps:
            state = "IPA available" if app.get("download") else "Manual setup"
            print("%-15s %-19s %s" % (app["id"], state, app["name"]))
        print("\nUse --all, --app ID, or --check. Downloads do not install apps.")
        return 0
    selected = [app for app in apps if not args.app or app["id"] in args.app]
    results, failed, manual = [], [], []
    for app in selected:
        print("\n" + app["name"], flush=True)
        if not app.get("download"):
            manual.append(app["name"])
            print("  MANUAL: " + app["notes"])
            print("  " + app["instructions"])
            continue
        try:
            if args.check:
                try:
                    with request(app["download"]["url"], "HEAD") as response:
                        print("  HTTP " + str(response.status))
                except urllib.error.HTTPError as error:
                    if error.code not in (405, 501):
                        raise
                    with request(app["download"]["url"]) as response:
                        response.read(1)
                        print("  HTTP " + str(response.status))
            else:
                results.append(download(app, args.output.resolve()))
        except (OSError, ValueError, zipfile.BadZipFile) as error:
            failed.append(app["name"])
            print("  FAILED: " + str(error), file=sys.stderr)
    if not args.check:
        args.output.mkdir(parents=True, exist_ok=True)
        (args.output / "download-report.json").write_text(
            json.dumps({"completed": results, "failed": failed, "manual": manual}, indent=2) + "\n",
            encoding="utf-8")
        print("\nDownloaded/verified: %d. Failed: %d. Manual: %d." %
              (len(results), len(failed), len(manual)))
        print("No app has been installed or signed. Read INSTALLAZIONE.md.")
    return 1 if failed else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nDownload interrupted.", file=sys.stderr)
        sys.exit(130)
