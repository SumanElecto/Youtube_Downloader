# YouTube Video Downloader

This Python script allows you to download YouTube videos in the best available quality using the [yt-dlp](https://github.com/yt-dlp/yt-dlp) library. It also ensures that `ffmpeg` is available for video/audio processing.

## Features

- Downloads YouTube videos in the best video and audio quality.
- Saves videos to your Downloads folder.
- Checks for `ffmpeg` in a specified directory before downloading.

## Requirements

- Python 3.7 or higher
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg](https://ffmpeg.org/) (must be installed and the path set in the script)

## Installation

1. **Install yt-dlp:**
    ```sh
    pip install yt-dlp
    ```

2. **Download and extract [ffmpeg](https://ffmpeg.org/download.html)**  
   Update the `ffmpeg_path` variable in the script to point to your `ffmpeg` binary directory.

## Usage

1. Edit the script if needed to set the correct `ffmpeg_path` and `save_path`.
2. Run the script:
    ```sh
    python Youtube_downloader.py
    ```
3. Enter the YouTube video URL when prompted.

## Script Details

- The script checks if `ffmpeg` is available in the specified directory.
- Downloads the video to `C:\Users\Admin\Downloads` (change `save_path` in the script if needed).
- The output file will be named after the video title.

## Troubleshooting

- If you see an error about `ffmpeg` not being found, make sure the `ffmpeg_path` variable is set to the directory containing the `ffmpeg` executable.
- Ensure you have the necessary permissions to write to the download directory.

## License

This script is provided as-is for personal use.
