from pytube import YouTube

input_url = input("Enter the url of the video: ")
youtube = YouTube(input_url)
youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
print("Download complete")
