from openai import OpenAI


MY_PROMPT = """
Given a user's spoken command related to Spotify playback control, 
generate the corresponding JSON format for the Spotify API. 
The supported commands are:

- play
- pause
- resume
- add to queue
- skip
- previous
- exit/quit

Ensure the JSON output has the fields: action, song, and artist.
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
