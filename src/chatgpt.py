from openai import OpenAI


MY_PROMPT = """
Given a user's spoken command related to Spotify playback control 
(e.g., play a specific track, pause, resume, add to queue, skip song), 
generate the corresponding JSON format for the Spotify API. 
The user's command might include details such as the action 
(play, pause, resume, add to queue), song name, artist name, etc. 
Ensure the JSON output has the fields: action, song, artist.
"""


class ChatGPT:
    def __init__(self) -> None:
        self.client = OpenAI()
        self.messages = [
            {"role": "system", "content": MY_PROMPT},
        ]

    def sendMessageToAI(self, message: str):
        if len(message) > 150:
            return

        user_message = {"role": "user", "content": message}

        self.messages.append(user_message)

        api_response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={"type": "json_object"},
            messages=self.messages,
        )

        message = api_response.choices[0].message
        self.messages.append(message)

        return message.content
