import yt_dlp
import os
import re
from urllib.parse import urlparse, parse_qs

# Configure yt-dlp options
YDL_OPTS = {
    'format': 'best',
    'outtmpl': 'downloads/%(title)s-%(id)s.%(ext)s',
    'quiet': True,
    'no_warnings': True,
    'ignoreerrors': True,
    'flat_playlist': True,
}

def is_youtube_url(url):
    """Check if the provided string is a YouTube URL."""
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    
    youtube_match = re.match(youtube_regex, url)
    return bool(youtube_match)

def is_youtube_playlist(url):
    """Check if the provided URL is a YouTube playlist."""
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return 'list' in query_params

def get_video_info(video):
    """Extract relevant information from a video."""
    if video is None:
        return None
    return {
        'id': video.get('id'),
        'title': video.get('title'),
        'thumbnail': video.get('thumbnail'),
        'duration': format_duration(video.get('duration')),
        'url': f"https://www.youtube.com/watch?v={video.get('id')}",
        'channel': video.get('channel'),
    }

def format_duration(seconds):
    """Format duration from seconds to HH:MM:SS."""
    if not seconds:
        return "Unknown"
    
    hours, remainder = divmod(int(seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    
    if hours:
        return f"{hours}:{minutes:02d}:{seconds:02d}"
    else:
        return f"{minutes:02d}:{seconds:02d}"

def fetch_videos(query):
    """Fetch videos from YouTube based on query or URL."""
    with yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True}) as ydl:
        try:
            if is_youtube_url(query):
                if is_youtube_playlist(query):
                    # Handle playlist
                    info = ydl.extract_info(query, download=False)
                    videos = info.get('entries', [])
                else:
                    # Handle single video
                    info = ydl.extract_info(query, download=False)
                    videos = [info]
            else:
                # Handle search query
                info = ydl.extract_info(f"ytsearch20:{query}", download=False)
                videos = info.get('entries', [])
            
            # Extract relevant information
            result = []
            for video in videos:
                if video:
                    if video is not None:
                        try:
                            result.append(get_video_info(video))
                        except:
                            print(f"Video unavailable: {video.get('id')}")
            return result
        except Exception as e:
            raise Exception(f"Error fetching videos: {str(e)}")

def download_video(video_id, quality='best'):
    """Download a video by its ID."""
    url = f"https://www.youtube.com/watch?v={video_id}"
    
    # Set format based on quality
    if quality == 'audio':
        options = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': 'downloads/%(title)s-%(id)s.%(ext)s',
            'quiet': True,
        }
    else:
        options = {
            'format': quality if quality != 'best' else 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': 'downloads/%(title)s-%(id)s.%(ext)s',
            'quiet': True,
        }
    
    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)
            
            # Adjust file extension for audio downloads
            if quality == 'audio':
                file_path = os.path.splitext(file_path)[0] + '.mp3'
            
            return file_path
    except Exception as e:
        raise Exception(f"Error downloading video: {str(e)}")
