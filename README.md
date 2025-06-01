# YouTube Video Downloader

A beautiful Flask web application that allows users to search for YouTube videos, watch them, and download them in various formats and quality options.

## Features

- Search for YouTube videos using keywords
- Parse YouTube playlist URLs to fetch all videos
- Display video metadata including thumbnails, titles, and durations
- Watch videos directly within the application
- Download videos in different quality options (Best, 720p, 360p)
- Download audio-only versions of videos (MP3)
- Responsive design that works on all device sizes
- Caching of search results for improved performance
- Loading indicators during operations
- Error handling for invalid URLs and failed operations

## Technologies Used

- Flask - Python web framework
- yt-dlp - YouTube video metadata extraction and downloading
- Jinja2 - Template engine
- Tailwind CSS - Utility-first CSS framework
- JavaScript - Client-side interactivity

## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/youtube-downloader.git
cd youtube-downloader
```

2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

4. Run the application:
```
python app.py
```

5. Open your browser and navigate to `http://127.0.0.1:5000`

## Project Structure

```
youtube-downloader/
├── app.py                  # Main Flask application
├── utils/
│   └── youtube.py          # YouTube video utilities
├── templates/
│   ├── base.html           # Base template
│   ├── index.html          # Home page
│   ├── results.html        # Search results page
│   └── watch.html          # Video watch page
├── static/
│   ├── css/
│   │   └── custom.css      # Custom CSS styles
│   └── js/
│       └── main.js         # JavaScript functionality
├── downloads/              # Directory for downloaded videos
└── requirements.txt        # Project dependencies
```

## Usage

1. Enter a YouTube video URL, playlist URL, or search term in the search box
2. Browse through the search results
3. Click "Watch" to view a video
4. Click "Download" and select a quality option to download a video

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This application is for educational purposes only. Please respect YouTube's terms of service and copyright laws when using this application.