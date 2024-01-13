# HeyDJ

HeyDJ is a voice controlled assistant for Spotify. Just say the phrase "Hey DJ" followed by a command to control your Spotify using voice commands!

## Prerequisites

- Python 3.x
- Spotify premium
- OpenAI API Key
- Picovoice account

## Installation

1. Clone the repository: `git clone https://github.com/your-username/HeyDJ.git`
2. Install dependencies: `pip install -r requirements.txt`

## First Time Setup

1. In the root directory of the application, create a `.env` file
2. Create a Spotify Developer Application [here](https://developer.spotify.com/)
3. Within the new Spotify Developer Application settings, set the `redirect URI` to `http://localhost/`
4. Set the following variables within your `.env` file:

   ```env
   SPOTIFY_CLIENT_ID='Your Spotify Client ID'
   SPOTIFY_CLIENT_SECRET='Your Spotify Client Secret'
   SPOTIFY_REDIRECT_URI=http://localhost/
   ```

  NOTE: Spotify Client ID and Spotify Client Secret can be found in your Spotify Developer Application settings

5. Create a OpenAI API key [here](https://openai.com/)
  - For instructions on creating the API key, click [here](https://www.maisieai.com/help/how-to-get-an-openai-api-key-for-chatgpt)

6. Set the following variables within your `.env` file:

  ```env
  OPENAI_API_KEY='Your OpenAI API key'
  ```

7. Sign up/ Sign In to your Picovoice account [here](https://picovoice.ai/)
8. Set the following variables within your `.env` file:

  ```env
  PICOVOICE_ACCESS_KEY='Your Picovoice Access key'
  ```

## Usage

1. Open up Spotify on your computer and have some music playing.
2. Start in the project root application
3. `cd src/`
4. `python3 main.py`
5. Say "Hey DJ" followed by your command to start using the assistant!
