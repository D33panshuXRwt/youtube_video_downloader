from pytube import YouTube

def download_youtube_video(video_url, output_filepath):

  youtube = YouTube(video_url)

  video_stream = youtube.streams.get_highest_resolution()

  video_stream.download(output_filepath)


video_url = input("Enter the Youtube Video URL: ")
output_filepath = "./video.mp4"

download_youtube_video(video_url, output_filepath)
