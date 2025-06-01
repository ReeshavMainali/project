from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for
import os
from utils.youtube import fetch_videos, download_video
from flask_caching import Cache

app = Flask(__name__)

# Configure cache
cache_config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 3600
}
app.config.from_mapping(cache_config)
cache = Cache(app)

# Create downloads directory if it doesn't exist
if not os.path.exists('downloads'):
    os.makedirs('downloads')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    if not query:
        return render_template('index.html', error="Please enter a search query or YouTube URL")
    
    return redirect(url_for('results', query=query))

@app.route('/results')
def results():
    query = request.args.get('query', '')
    if not query:
        return redirect(url_for('index'))
    
    return render_template('results.html', query=query)

@app.route('/api/videos')
def get_videos():
    query = request.args.get('query', '')
    if not query:
        return jsonify({"error": "No query provided"}), 400
    
    # Check cache first
    cached_result = cache.get(f"search:{query}")
    if cached_result:
        return jsonify(cached_result)
    
    try:
        videos = fetch_videos(query)
        # Cache the result
        cache.set(f"search:{query}", videos)
        return jsonify(videos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/download/<video_id>')
def download(video_id):
    try:
        # Get video quality from query parameters, default to best
        quality = request.args.get('quality', 'best')
        file_path = download_video(video_id, quality)
        filename = os.path.basename(file_path)
        return send_file(
            file_path,
            as_attachment=True,
            download_name=filename,
            mimetype='video/mp4'
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/watch/<video_id>')
def watch(video_id):
    try:
        return render_template('watch.html', video_id=video_id)
    except Exception as e:
        return render_template('error.html', error=f"Video unavailable: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
