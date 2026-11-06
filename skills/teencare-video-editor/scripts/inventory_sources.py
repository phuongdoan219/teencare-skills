"""Record media metadata with FFprobe; does not identify actions or edit sources."""

import argparse
import json
import os
import shutil
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

EXTENSIONS = {".mp4", ".mov", ".m4v", ".mkv", ".avi", ".webm", ".mts", ".m2ts",
              ".mp3", ".wav", ".m4a", ".aac", ".ogg", ".flac", ".jpg", ".jpeg",
              ".png", ".webp", ".tif", ".tiff", ".bmp", ".gif"}
IMAGES = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff", ".bmp", ".gif"}


def find_ffprobe(override):
    candidates = ([override] if override else [os.environ.get("HYPERFRAMES_FFPROBE_PATH"),
                  "E:/HYPERFRAME/tools/bin/ffprobe.exe", shutil.which("ffprobe")])
    for candidate in candidates:
        if candidate and (Path(candidate).is_file() or shutil.which(candidate)):
            return str(candidate)
    raise FileNotFoundError("FFprobe unavailable; provide --ffprobe with its executable path")


def number(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def fps(value):
    try:
        return float(Fraction(value))
    except (TypeError, ValueError, ZeroDivisionError):
        return None


def probe(path, executable):
    record = {"path": str(path), "bytes": path.stat().st_size,
              "kind": "image" if path.suffix.lower() in IMAGES else "media"}
    try:
        process = subprocess.run([executable, "-v", "error", "-show_format", "-show_streams",
                                  "-of", "json", str(path)], capture_output=True, timeout=60)
        if process.returncode:
            raise ValueError(process.stderr.decode("utf-8", errors="replace").strip() or "FFprobe failed")
        data = json.loads(process.stdout)
        streams = []
        for source in data.get("streams", []):
            stream = {key: source[key] for key in ("index", "codec_type", "codec_name", "width", "height",
                      "pix_fmt", "sample_rate", "channels", "channel_layout", "color_space",
                      "color_transfer", "color_primaries") if key in source}
            stream["duration_seconds"] = number(source.get("duration"))
            if source.get("codec_type") == "video":
                stream["fps"] = fps(source.get("avg_frame_rate")) or fps(source.get("r_frame_rate"))
                rotation = source.get("tags", {}).get("rotate")
                for side_data in source.get("side_data_list", []):
                    if "rotation" in side_data:
                        rotation = side_data["rotation"]
                stream["rotation_degrees"] = number(rotation) if rotation is not None else 0
            streams.append(stream)
        record.update({"duration_seconds": number(data.get("format", {}).get("duration")),
                       "has_audio": any(s.get("codec_type") == "audio" for s in streams), "streams": streams})
    except (OSError, ValueError, subprocess.TimeoutExpired) as error:
        record["error"] = str(error)
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="One or more source files/folders")
    parser.add_argument("--recursive", action="store_true")
    parser.add_argument("--output", required=True, type=Path, help="New JSON path; existing files are preserved")
    parser.add_argument("--ffprobe")
    args = parser.parse_args()
    try:
        if args.output.exists():
            raise FileExistsError(f"Output already exists: {args.output}")
        executable = find_ffprobe(args.ffprobe)
        files = set()
        for source in args.paths:
            if not source.exists():
                raise FileNotFoundError(f"Input unavailable: {source}")
            candidates = source.rglob("*") if source.is_dir() and args.recursive else (
                source.glob("*") if source.is_dir() else [source])
            for path in candidates:
                if path.is_file() and path.suffix.lower() in EXTENSIONS:
                    files.add(path.resolve())
        if not files:
            raise ValueError("No supported media files found")
        records = [probe(path, executable) for path in sorted(files, key=lambda p: str(p).casefold())]
        result = {"ffprobe": executable, "content_review_required": True, "files": records}
        with args.output.open("x", encoding="utf-8") as handle:
            json.dump(result, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        errors = sum("error" in record for record in records)
        print(f"Saved {len(records)} file(s), {errors} probe error(s): {args.output}")
        return 1 if errors else 0
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
