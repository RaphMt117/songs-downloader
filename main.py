from dotenv import load_dotenv
import yaml
import subprocess
import requests
import os

with open("songs.yml", "r") as file:
    data = yaml.safe_load(file)

load_dotenv()
api_key = os.getenv("API_KEY")
destination_folder = os.getenv("DESTINATION_FOLDER")

if api_key is None:
    raise ValueError("API_KEY environment variable is not set.")
if destination_folder is None:
    raise ValueError("DESTINATION_FOLDER environment variable is not set.")


# Query YouTube API and return the first URL
def query_youtube(artist, song, api_key):
    base_url = "https://www.googleapis.com/youtube/v3/search"
    query = f"{artist} {song}"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "order": "relevance",
        "maxResults": 1,
        "key": api_key,
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        results = response.json().get("items", [])

        if results:
            # Extract the videoId for the first result
            video_id = results[0]["id"]["videoId"]
            return f"https://www.youtube.com/watch?v={video_id}"

    print(f"No results found for: {artist} - {song}")
    return None


def download_mp3(url, destination_folder):
    try:
        command = [
            "yt-dlp",
            url,
            "-x",  # Extract audio
            "--audio-format",
            "mp3",  # Convert audio to MP3
            "-o",
            f"{destination_folder}/%(title)s.%(ext)s",  # Output format
        ]
        result = subprocess.run(command, check=True, capture_output=True)
        print(f"Downloading MP3 with yt-dlp: {result.stdout}")

    except subprocess.CalledProcessError as e:
        print(f"Error while downloading {url}: {e.stderr}")


for artist, songs in data.get("artists", {}).items():
    for song in songs:
        print(f"Querying for: {artist} - {song}")
        url = query_youtube(artist, song, api_key)
        if url:
            print(f"Found URL for {artist} - {song}: {url}")
            download_mp3(url, destination_folder)
