from pytube import YouTube
import os
from pathlib import Path
link = input("Enter link here: ")
print("Link")
try:
    url = YouTube(link)
    print("downloading....")
    video = url.streams.get_highest_resolution()
    path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
    video.download(path_to_download_folder)
    print("Downloaded! :)")
except Exception as e:
    print(f"Error {e}")