import os
import random
from moviepy.editor import *
from moviepy.video.tools.subtitles import *
from PIL import Image, ImageFilter
import numpy as np

def apply_blur(image):
        # Convert numpy array to PIL image
        pil_image = Image.fromarray(image)
        # Apply Gaussian blur
        pil_image = pil_image.filter(ImageFilter.GaussianBlur(radius=50))
        # Convert back to numpy array
        return np.array(pil_image)

def write_video(clip_directory: str, subtitles_path: str, output_path: str, font: str):
    duration = 0
    iteration = 1
    # Get duration of voiceover
    with open (subtitles_path, 'r') as subs:
        subs_duration = subs.readlines()[-3][-12:].replace(',', '.')
        h, m, s = subs_duration.split(':')
        subs_duration = int(h) * 3600 + int(m) * 60 + float(s)

    """ while duration < subs_duration:
        # Get clip files
        clips: list[str] = os.listdir(clip_directory)
        clips = [os.path.join(clip_directory, clip) for clip in clips]
        # Take random clips
        clips = random.sample(clips, 12)
        # Create VideoFileClips from files
        video_file_clips: list[VideoFileClip] = [VideoFileClip(clip, target_resolution=(1920, 1080)).set_fps(30) for clip in clips]

        # Set max duration of individual clips to 5 seconds
        video_file_clips = [clip.set_end(5) if float(clip.duration) > 5.0 else clip for clip in video_file_clips]
        # compute duration of video
        duration = sum([float(clip.duration) for clip in video_file_clips])
        print(iteration, "done,", duration, "seconds")
        iteration += 1
    print("found clips")
    # Put all clips together
    concatenated_videoclip: VideoClip = concatenate_videoclips(video_file_clips)

    # Cap video duration to length of voiceover
    concatenated_videoclip = concatenated_videoclip.set_duration(subs_duration)
    print(float(concatenated_videoclip.duration), "seconds")
    # Close VideoFileClips
    [clip.close() for clip in video_file_clips] """


    # Add subtitles text to video
    generator = lambda txt: TextClip(txt, font=font, fontsize=48, color='white', align="center", size=(500, None), method="caption")
    generator_glow = lambda txt: TextClip(txt, font=font, fontsize=48, color='red', align="center", size=(500, None), method="caption")

    sub = SubtitlesClip(subtitles_path, generator)
    sub_glow = SubtitlesClip(subtitles_path, generator_glow).fl_image(apply_blur)

    final_video = CompositeVideoClip([sub_glow.set_pos(('center','center'))]).set_end(1)

    # Write video file
    final_video.write_videofile(output_path, audio=False, fps=30)
    


if __name__ == "__main__":
    write_video("clips", "subtitle.srt", "output/video-subs.mp4", "Staatliches-Regular")
