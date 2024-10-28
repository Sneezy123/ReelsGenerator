
from elevenlabs.client import ElevenLabs
import os
import dotenv

def save_file_voiceover(text: str, save_file_path = "output/voiceover.mp3"):
    dotenv.load_dotenv()

    elevenlabs_key = os.getenv("XI_LABS_KEY")

    client = ElevenLabs(
    api_key=elevenlabs_key, # Defaults to ELEVEN_API_KEY
    )

    audio = client.generate(
    text=text,
    voice="Chris",
    output_format="mp3_22050_32",
    model="eleven_multilingual_v2"
    )

        # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in audio:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")