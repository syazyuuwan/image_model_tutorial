import os
from openai import OpenAI
import dalle_model as dalle
import vision_model as vision

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"),
                organization=os.getenv("OPENAI_ORGANIZATION"))

# Generate an image with dall e 3

msg = "Island scenery"
#dalle.img_ai(msg)

# Openai Vision

#vision with image url

url = "https://letsenhance.io/static/8f5e523ee6b2479e26ecc91b9c25261e/1015f/MainAfter.jpg"
#vision.vision_url(url,client)

#vision with image file
#vision.vision_file("Designer.jpeg",client)

from pathlib import Path
from openai import OpenAI

client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Today is a wonderful day to build something people love!")

with open(speech_file_path, "wb") as file:
    file.write(response.content)
