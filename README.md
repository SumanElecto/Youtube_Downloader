# YouTube Video Downloader

This Python script downloads YouTube videos using [yt-dlp](https://github.com/yt-dlp/yt-dlp) and ffmpeg for media processing.

## Features

- Downloads YouTube videos in the best available quality
- Saves videos to a chosen folder
- Supports ffmpeg auto-detection or an explicit path
- Works on Windows, macOS, and Linux

## Requirements

- Python 3.8+
- [ffmpeg](https://www.ffmpeg.org/download.html)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)

## Installation

1. Install ffmpeg and make sure it is available in your PATH, or note the folder containing the `ffmpeg` executable.
2. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with a YouTube URL:

```bash
python Youtube_Downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

Optional arguments:

```bash
python Youtube_Downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" --output-dir ~/Downloads --ffmpeg-path /usr/local/bin
```

If you do not provide a URL, the script will prompt you for one.

## Troubleshooting

- If ffmpeg is not found, install it and ensure it is on PATH.
- If the script cannot find ffmpeg, pass `--ffmpeg-path` pointing to the directory or executable.
- Some YouTube videos may be restricted or require a valid network connection.

## License

This script is provided as-is for personal use.
