import argparse
import os
import shutil
import sys
from pathlib import Path

import yt_dlp


DEFAULT_DOWNLOAD_DIR = Path.home() / "Downloads"


def find_ffmpeg(ffmpeg_path: str | None = None) -> str | None:
    """Return the ffmpeg binary path or None if not available."""
    candidates = []

    if ffmpeg_path:
        ffmpeg_dir = Path(ffmpeg_path).expanduser()
        candidates.extend(
            [
                str(ffmpeg_dir / "ffmpeg"),
                str(ffmpeg_dir / "ffmpeg.exe"),
            ]
        )

    candidates.extend(["ffmpeg", "ffmpeg.exe"])

    for candidate in candidates:
        resolved = shutil.which(candidate)
        if resolved:
            return resolved

        # support direct paths passed in via ffmpeg_path
        if isinstance(candidate, str) and Path(candidate).is_file():
            return candidate

    return None


def add_ffmpeg_to_path(ffmpeg_binary: str) -> None:
    ffmpeg_dir = str(Path(ffmpeg_binary).resolve().parent)
    os.environ["PATH"] = ffmpeg_dir + os.pathsep + os.environ.get("PATH", "")


def download_video(url: str, output_dir: Path, ffmpeg_path: str | None = None) -> None:
    ffmpeg_binary = find_ffmpeg(ffmpeg_path)
    if not ffmpeg_binary:
        raise FileNotFoundError(
            "ffmpeg was not found. Install ffmpeg and make sure it is available on PATH, "
            "or pass --ffmpeg-path to the directory containing the ffmpeg executable."
        )

    add_ffmpeg_to_path(ffmpeg_binary)
    output_dir.mkdir(parents=True, exist_ok=True)

    ydl_opts = {
        "format": "bv*+ba/b",
        "outtmpl": str(output_dir / "%(title)s.%(ext)s"),
        "noplaylist": True,
        "quiet": False,
        "no_warnings": False,
        "merge_output_format": "mp4",
        "postprocessors": [
            {
                "key": "FFmpegVideoConvertor",
                "preferedformat": "mp4",
            }
        ],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Download completed successfully: {url}")
    except yt_dlp.utils.DownloadError as exc:
        print(f"Download failed: {exc}", file=sys.stderr)
        raise


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download a YouTube video with yt-dlp and ffmpeg support."
    )
    parser.add_argument("url", nargs="?", help="YouTube video URL")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_DOWNLOAD_DIR,
        help="Directory where the video should be saved (default: ~/Downloads)",
    )
    parser.add_argument(
        "--ffmpeg-path",
        help="Path to ffmpeg binary directory or executable",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    url = args.url or input("URL: ").strip()
    if not url:
        print("No URL provided.", file=sys.stderr)
        return 1

    try:
        download_video(url, args.output_dir, args.ffmpeg_path)
        return 0
    except FileNotFoundError as exc:
        print(exc, file=sys.stderr)
        return 1
    except Exception as exc:  # pragma: no cover - best effort user-facing error
        print(f"Unexpected error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
