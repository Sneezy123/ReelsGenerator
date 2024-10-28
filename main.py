# This is the main python file for this project
# Project content: This project will be an automated generator for instagram reels, tiktok posts or youtube shorts. It will use AI to select clips, add music, add captions, a voice-over, and icons with sound effects.

# I will start with the clip editing...

# Packages that will be used: moviepy, SOME TEXT TO SPEECH SERVICE (PREFERABLY ELEVENLABS), SOME AI SCRIPT WRITING SERVICE (LIKE MS COPILOT OR CHAT GPT), SOME CAPTIONING (SUBTITLE GENERATOR) SERVICE (PROBABLY OPEN AI WHISPER)
# Images of icons will need descriptions, so I will need a service that can generate text from images (like CLIP)

from generate_script import return_script
from generate_voiceover import save_file_voiceover
from generate_srt_file import generate_srt
from put_clips_together import write_video



if __name__ == "__main__":
    prompt: str
    audio_file_path: str = "output/voiceover.mp3"
    subtitle_file_path: str = "output/subtitle.srt"
    video_file_path: str = "output/video.mp4"

    with open("./input/prompt.txt", "r") as f:
        prompt = f.read()
        print("Prompt read.")


    script: str = return_script(prompt)
    print("Script generated.")
    print(script)

    save_file_voiceover(script, audio_file_path)
    print("Voiceover generated.")
    
    generate_srt(audio_file_path=audio_file_path, output_file_path=subtitle_file_path)
    print("Subtitles generated.")

    write_video("./input/clips", subtitle_file_path, "./input/Background Music", audio_file_path, video_file_path, "Staatliches-Regular", 120, "white", "black", 4, False, 11, 12, 5)
