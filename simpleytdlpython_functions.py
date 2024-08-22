"""

Python code By SirHenricus On GitHub.
Some parts of the code were written using ChatGPT

A simple interface for yt-dlp that I made to take advantage of it's feature

"""


import yt_dlp

import os

## -------FUNCTIONS

def download_video(video_url):
    ydl_opts = {
        'format': 'best',  # Download the best quality available
        'outtmpl': '%(title)s.%(ext)s'  # Save the audio in the 'output' folder with the video title as the filename
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])


def download_video_with_metadata(video_url):
    ydl_opts = {
        'format': 'best',  # Download the best quality available
        'outtmpl': '%(title)s.%(ext)s',  # Save the video with its title as the file name
        'writeinfojson': True,  # Write video metadata to a JSON file
        'writethumbnail': True,  # Download the thumbnail image
        'writesubtitles': True,  # Download subtitles if available
        'writeannotations': True,  # Download annotations if available
        'addmetadata': True,  # Add metadata to the video file
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
def download_audio_from_video(video_url):
    # Get the current directory where the script is located
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Define the output folder path
    download_folder = os.path.join(current_directory, 'output')
    
    # Ensure the 'output' folder exists
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    ydl_opts = {
        'format': 'bestaudio/best',  # Download the best available audio quality
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Save the audio in the 'output' folder with the video title as the filename
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Extract audio using FFmpeg
            'preferredcodec': 'mp3',      # Convert the audio to mp3 format
            'preferredquality': '192',    # Set audio quality to 192kbps
        }],
        'addmetadata': True,  # Embed metadata into the audio file
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def download_playlist(playlist_url):
    # Initialize yt-dlp options
    ydl_opts = {
        'outtmpl': '%(playlist_title)s/%(title)s.%(ext)s',  # Create a folder with the playlist name
        'writedescription': True,  # Write video description to a .description file
        'writeinfojson': True,  # Write video metadata to a .info.json file
        'writeannotations': True,  # Write video annotations to a .annotations.xml file
        'writesubtitles': True,  # Download subtitles if available
        'subtitlesformat': 'best',  # Best format for subtitles
        'subtitleslangs': ['en'],  # Download only English subtitles, adjust if needed
        'format': 'best',  # Download the best quality format
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

def download_channel_videos(channel_url):
    # Create an 'output' folder in the current directory
    output_folder = 'output'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Create a unique folder for the channel's videos inside 'output'
    channel_folder = os.path.join(output_folder, 'channel_videos')
    if not os.path.exists(channel_folder):
        os.makedirs(channel_folder)

    # yt-dlp options
    ydl_opts = {
        'outtmpl': os.path.join(channel_folder, '%(title)s.%(ext)s'),  # Save with title as filename
        'writeinfojson': True,  # Write metadata to a JSON file
        'writedescription': True,  # Write description to a .description file
        'writeannotations': True,  # Write annotations to a .annotations file
        'writesubtitles': True,  # Write subtitles
        'subtitleslangs': ['en'],  # Download only English subtitles
        'writeautomaticsub': True,  # Download automatic captions if no other subtitles are available
        'format': 'best',  # Download the best quality available
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([channel_url])


## ------USER INTERFACE 

if __name__ == "__main__":
    print("--SIMPLE YT-DLP PYTHON INTERFACE--")

    
    alpha = int(input("""
    Choose Download Style:

    1 - Single Video
    2 - Single Video With Metadata
    3 - Single Video (Audio Only)
    4 - Playlist
    5 - Channel

    type your desired number to select
    """))

    if alpha == 1:
     print("Singular Video Download Selected!")
     urlin = input("Enter the YouTube Video URL: ")
     download_video(urlin)
     print("Download Done!")
    if alpha == 2:
      print("Singular Video With Metadata Download Selected!")
      urlin = input("Enter the YouTube Video URL: ")
      download_video_with_metadata(urlin)
      print("Download Done!")
    if alpha == 3:
      print("Singular Video With Audio Only Download Selected!")
      urlin = input("Enter the YouTube Video URL: ")
      download_audio_from_video(urlin)
      print("Download Done!")
    if alpha == 4:
      print("Playlist Videos Download Selected!")
      urlin = input("Enter the YouTube Playlist URL: ")
      download_playlist(urlin)
      print("Download Done!")
    if alpha == 5:
      print("Channel Videos Download Selected!")
      urlin = input("Enter the YouTube Channel URL: ")
      download_channels(urlin)
      print("Download Done!")
