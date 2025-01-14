# Songs downloader

made for personal use only

## How to use

- You need to have [youtube-dl](https://github.com/ytdl-org/youtube-dl) installed and
  the executable (`yt-dl`) in your path

- Python packages:

  - dotenv
  - yaml
  - subprocess
  - requests

- Set a songs.yml file with the following structure:

```yaml
artists:
  { artist1 name }:
    - { song1 name }
    - { song2 name }
    - { ... }
  { artist2 name }:
    - { song1 name }
    - { song2 name }
    - { ... }
  { ... }
```

- You need to set a .env file with:
  - `API_KEY`: your google api key, with permission to use youtube api
  - `DESTINATION_FOLDER`: the path to the folder that will store your songs
