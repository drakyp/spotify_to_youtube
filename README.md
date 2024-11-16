# Spotify to YouTube Music Downloader

This project retrieves song information from your Spotify playlists, searches for each song on YouTube, and downloads the audio in MP3 format. It leverages the Spotify API for playlist access, `yt-dlp` for YouTube downloads, and several other Python libraries for web scraping and data handling.

## Project Overview

The project is divided into two main parts:
1. **Spotify API Integration**: Retrieves song information (like title, artist, and album) from your Spotify playlists and saves it to a CSV file.
2. **YouTube Downloading**: Reads song titles from the CSV file, searches for each song on YouTube, and downloads the audio as an MP3 file.

## Libraries to Install

To run this project, you need to install the following libraries:

1. **BeautifulSoup** - For HTML parsing.
   ```bash
   pip install beautifulsoup4
   ```

2. **requests-html** - For handling JavaScript-rendered pages in YouTube search.
   ```bash
   pip install requests-html
   ```

3. **yt-dlp** - A tool to download audio and video from YouTube and other platforms (a fork of youtube-dl).
   ```bash
   pip install yt-dlp
   ```

4. **pandas** - For reading and writing song information to a CSV file.
   ```bash
   pip install pandas
   ```

5. **spotipy** - For Spotify API integration.
   ```bash
   pip install spotipy
   ```

6. **ffmpeg** (external tool) - For converting downloaded audio to MP3. Install this based on your operating system:
   - **macOS**: `brew install ffmpeg`
   - **Linux (Debian/Ubuntu)**: `sudo apt install ffmpeg`
   - **Windows**: Download and add to PATH from [ffmpeg.org](https://ffmpeg.org/download.html).

## File Structure and Functions

### Main Components

1. **ScrapeVidId(query)**:
   - This function accepts a song title as a search query, sends a request to YouTube, and retrieves the first video result.
   - Uses `requests-html` to handle JavaScript and `BeautifulSoup` to parse the HTML.

2. **DownloadVideosFromTitles(list_of_songs)**:
   - Takes a list of song titles, scrapes YouTube for each, and collects video URLs for downloading.
   - Calls `DownloadsVideoFromIds` to download the videos.

3. **DownloadsVideoFromIds(list_of_videos)**:
   - Downloads audio for each video URL in `list_of_videos` using `yt-dlp`.
   - Extracts audio and converts it to MP3 format in a `Downloads/songs` directory.

4. **Spotify API Functions**:
   - **create_spotify_oauth()**: Sets up the Spotify OAuth for accessing the user’s playlists.
   - **getTracks()**: Retrieves the user’s playlists and each playlist's songs.
   - **get_album_track()**: Extracts details for each song in a playlist and saves them to `songs.csv`.

### Running the Script

1. **Spotify OAuth Setup**:
   - When you run the Flask app, navigate to the `/` endpoint to authenticate with Spotify.
   - After login, `getTracks()` will retrieve your playlist details and save song information in `songs.csv`.

2. **Downloading from YouTube**:
   - After `songs.csv` is created, run the `__main__` function, which reads song titles and downloads each one from YouTube in MP3 format.

### Example Usage

1. **Start the Flask Server**:
   ```bash
   flask run
   ```
   - Open a browser and go to `http://127.0.0.1:5000/` to log in to Spotify.

2. **Run YouTube Downloader**:
   ```bash
   python your_script_name.py
   ```
   - This will read `songs.csv` and download each song as an MP3 in the `Downloads/songs` folder.

## Notes

- Ensure `ffmpeg` is installed to convert audio to MP3.
- Some parts of YouTube scraping may be blocked by YouTube policies, so be mindful of using these scripts responsibly.
- The Flask app and the YouTube downloader may need to be run in separate sessions.

## Troubleshooting

- **YouTube Errors**: If `yt-dlp` fails to download, ensure it is up-to-date with `pip install -U yt-dlp`.
- **Spotify Authentication Issues**: Clear the session or restart the server if session errors occur.



