Billboard Top 100 to Spotify Playlist

This Python program allows users to create a Spotify playlist based on the Billboard Top 100 chart for a user-specified week. Users input a date, and the program scrapes the Billboard website for the top songs of that week, then adds those songs to a new playlist on their Spotify account.

## Objective

The objective of this project is to automate the creation of Spotify playlists based on historical Billboard Top 100 charts. Users can specify any week, and the program will generate a playlist with the top songs from that time.

## Tech Stack

- **Python**: The core programming language used for the project.
- **BeautifulSoup**: A Python library for web scraping to extract song data from the Billboard website.
- **Requests**: A simple HTTP library for Python to handle web requests.
- **Spotipy**: A lightweight Python library for the Spotify Web API to create and manage playlists on Spotify.

## Skills Demonstrated

- **Web Scraping**: Using BeautifulSoup and Requests to scrape data from the Billboard website.
- **Spotify API Integration**: Using Spotipy to authenticate with the Spotify API, search for songs, and create playlists.
- **User Input Handling**: Accepting and processing user input to specify the desired week for the Billboard chart.
- **Error Handling**: Managing potential errors such as missing songs on Spotify.

## How to Run the Project

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install Dependencies**:
    Ensure you have Python installed. Then, install the required libraries using pip:
    ```bash
    pip install beautifulsoup4 requests spotipy
    ```

3. **Setup Spotify Developer Account**:
    - Create an application on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
    - Note down your `client_id`, `client_secret`, and `redirect_uri`.

4. **Configure the Script**:
    - Replace the placeholder values for `client_id`, `client_secret`, and `redirect_uri` in the script with your actual Spotify application credentials.

5. **Run the Script**:
    ```bash
    python main.py
    ```

6. **Input Date**:
    - When prompted, enter the desired date in `YYYY-MM-DD` format to fetch the Billboard Top 100 for that week.

## Notes

- Ensure that the redirect URI in your Spotify Developer Dashboard matches the one provided in the script.
- The playlist will be created as a private playlist. You can change this by setting the `public` parameter to `True` in the `sp.user_playlist_create` method.