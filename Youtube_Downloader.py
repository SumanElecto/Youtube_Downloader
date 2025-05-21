import yt_dlp
import shutil
import os

def yt_download():
    ffmpeg_path = "D:\\Apps\\ffmpeg_2023\\bin"  # Update this to the directory containing ffmpeg binary
    if not shutil.which("ffmpeg", path=ffmpeg_path):
        print("ffmpeg is not installed in the specified directory. Please check the path.")
        return

    os.environ["PATH"] += os.pathsep + ffmpeg_path

    save_path = "C:\\Users\\Admin\\Downloads"
    link = input("URL: ")
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': save_path + '/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print("Success")

yt_download()
