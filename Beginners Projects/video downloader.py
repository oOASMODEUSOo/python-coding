import pytube
#from pytube import YouTube
video_url = input("Enter Video Link: ")
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download('C:/Users/allfo/Desktop/')