#!/usr/bin/python3
from pytube import YouTube
from colorama import Fore
import os, sys

def Youtube_download():
    save_path = os.getcwd()
    link = input("Enter the link: ")
    try:
        yt = YouTube(link)
    except:
        print(Fore.RED + "Connection Error! please verify if URL is correct." + Fore.RESET)
        sys.exit()
    else:
        print(Fore.GREEN + "URL is OK" + Fore.RESET)
    #Title of the video
    print(Fore.CYAN + "Title:" + Fore.RESET, yt.title)
    #Length of the video
    print(Fore.CYAN + "Length:" + Fore.RESET, round(yt.length/60, 2), "mins")
    # Views
    print(Fore.CYAN + "Views:" + Fore.RESET, yt.views)
    #Rating
    print(Fore.CYAN + "Rating:" + Fore.RESET, yt.rating)
    try:
        print(Fore.YELLOW + "Downloading..." + Fore.RESET)
        ys = yt.streams.get_highest_resolution()
        ys.download(save_path)
    except:
        print(Fore.RED + "Something went wrong" + Fore.RESET)
    else:
        print(Fore.GREEN + "Download completed and saved to {}".format(save_path) + Fore.RESET)

if __name__ =="__main__":
    Youtube_download()