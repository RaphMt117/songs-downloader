# Songs downloader

Made for personal use only

## How to use

- You need to have [yt-dlp](https://github.com/yt-dlp/yt-dlp) installed and
  the executable (`yt-dlp`) in your path

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

- Have a valid api key from google [doc](https://support.google.com/googleapi/answer/6158862?hl=en)

- Enable youtube data api, see [doc](https://support.google.com/googleapi/answer/6158841?hl=en&ref_topic=7013279&sjid=16203019970447198290-SA)

### Env file

- Mandatory:

  - `API_KEY`: your google api key, with permission to use youtube api

- Optional:

  - `DESTINATION_FOLDER`: the path to the folder that will store your songs
