from dotenv import load_dotenv
import yaml
import subprocess
import requests
import os

load_dotenv()
api_key = os.getenv("API_KEY")
destination_folder = os.getenv("DESTINATION_FOLDER")

if api_key is None:
    raise ValueError("API_KEY environment variable is not set.")
if destination_folder is None:
    destination_folder = os.path.expanduser

with open("songs.yml", "r") as file:
    data = yaml.safe_load(file)


def get_url_by_song(artist, song, api_key):
    base_url = "https://www.googleapis.com/youtube/v3/search"
    query = f"{artist} {song}"
    params = {
        "part": "id",
        "q": query,
        "type": "video",
        "maxResults": 1,
        "fields": "items/id/videoId",
        "key": api_key,
    }

    print(f"Querying for: {artist} - {song}")
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        results = response.json().get("items", [])

        if results:
            video_id = results[0]["id"]["videoId"]
            url = f"https://www.youtube.com/watch?v={video_id}"

            print(f"Found url: {url}")
            return url

    print(f"No results found for: {artist} - {song}")
    return None


def download_mp3_from_url(url):
    try:
        command = [
            "yt-dlp",
            url,
            "-x",
            "--audio-format",
            "mp3",  # extract audio + mp3 format
            "-o",
            f"{destination_folder}/%(title)s.%(ext)s",  # output folder + file name format
        ]
        print(f"Downloading MP3 with yt-dlp for {url}")
        result = subprocess.run(command, check=True, capture_output=True)
        result.check_returncode

        print("Download completed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error while downloading {url}: {e.stderr}")


for artist, songs in data.get("artists", {}).items():
    for song in songs:
        url = get_url_by_song(artist, song, api_key)
        if url:
            download_mp3_from_url(url)
