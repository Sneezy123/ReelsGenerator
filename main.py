# This is the main python file for this project
# Project content: This project will be an automated generator for instagram reels, tiktok posts or youtube shorts. It will use AI to select clips, add music, add captions, a voice-over, and icons with sound effects.

# I will start with the clip editing...

# Packages that will be used: moviepy, SOME TEXT TO SPEECH SERVICE (PREFERABLY ELEVENLABS), SOME AI SCRIPT WRITING SERVICE (LIKE MS COPILOT OR CHAT GPT), SOME CAPTIONING (SUBTITLE GENERATOR) SERVICE (PROBABLY OPEN AI WHISPER)
# Images of icons will need descriptions, so I will need a service that can generate text from images (like CLIP)

from generate_script import return_script
from generate_voiceover import save_file_voiceover
from generate_srt_file import generate_srt



if __name__ == "__main__":
    prompt: str

    with open("./prompt.txt", "r") as f:
        prompt = f.read()
        print("Prompt read.")


    script: str = return_script(prompt)
    print("Script generated.")
    print(script)

    #save_file_voiceover(script) # Deactivated because it drains my tokens
    #print("Voiceover generated.")
    
    generate_srt(audio_file_path="output/eb85ca1e-84b8-45af-af76-5b782a8946a2.mp3", output_file_path="output/subtitle.srt")
    print("Subtitles generated.")
