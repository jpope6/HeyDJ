# HeyDJ

HeyDJ is a voice controlled assistant for Spotify. Just say the phrase "Hey DJ" followed by a command to control your Spotify using voice commands! The command you give will be processed by OpenAI, enabling the assistant to understand and interpret your command without the need for an exact phrase match. Experience a seamless and intuitive interaction as HeyDJ combines voice recognition and OpenAI's powerful language processing, providing a natural and personalized Spotify control experience.

![](https://github.com/jpope6/HeyDJ/blob/main/src/images/HeyDJ.gif)

## Prerequisites

- Python 3.x
- Spotify premium
- OpenAI API Key
- Picovoice account

## Installation

1. Clone the repository: `git clone https://github.com/your-username/HeyDJ.git`
2. Install dependencies: `pip install -r requirements.txt`

Please be patient, as the installation process involves downloading and setting up the required language processing libraries.

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
   **NOTE:** Spotify Client ID and Spotify Client Secret can be found in your Spotify Developer Application settings

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

## Commands

The following are commands that your DJ assistant will understand. Remember, you do NOT have to say the commands exactly as they are written; OpenAI will interpret your command intelligently.

- `play/resume`: Resume playback or play a specific song.
  - Example: "Hey DJ, play my music."
- `pause`: Pause the currently playing song
  - Example: "Hey DJ, pause the music."
- `play a song or artist`: Play a specific song or artist
  - Example: "Hey DJ, play I Gotta Feeling by The Black Eyed Peas."
- `add song to queue`: Add a song to the queue for continuous playback
  - Example: "Hey DJ, add Boom Boom Pow by The Black Eyed Peas to the queue."
- `skip song`: Skip to the next song in the playlist.
  - Example: "Hey DJ, skip this song."
- `previous song`: Go back to the previous song.
  - Example: "Hey DJ, play the previous track."
- `exit`: Exit the application.
  - Example: "Hey DJ, exit."

## Future plans

- Add more commands
- Improve User Interface

## Contributing

I appreciate your interest in contributing to HeyDJ! While for the time being, I'm keeping this project as a solo endeavor, I'm always open to hearing your suggestions and feedback. If you have ideas or improvements in mind, feel free to share them – your input is valuable. Thank you for your understanding!

## License

[MIT](https://choosealicense.com/licenses/mit/)
