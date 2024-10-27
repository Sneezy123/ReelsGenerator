import os
import random
from moviepy.editor import *
from moviepy.video.tools.subtitles import *
import cv2
from pydub import AudioSegment


def _make_clips(clip_directory: str, subtitles_path: str, voice_over_path: str, font: str, font_size: int, text_color: str, stroke_color: str, stroke_width: int, glow_spread: int, num_clips: int, max_clip_duration: float):
    duration = 0
    iteration = 1
    # Get duration of voiceover
    audio_file = AudioSegment.from_file(voice_over_path)
    voice_duration = audio_file.duration_seconds
    

    print(voice_duration, "seconds needed.\nSearching for random clips until they are long enough.")
    while duration < voice_duration:
        # Get clip files
        clips = [os.path.join(clip_directory, clip) for clip in os.listdir(clip_directory)]
        # Take random clips
        clips = random.sample(clips, num_clips)
        # Create VideoFileClips from files
        video_file_clips: list[VideoFileClip] = [VideoFileClip(clip, target_resolution=(1920, 1080)).set_fps(30) for clip in clips]

        # Set max duration of individual clips to 5 seconds
        video_file_clips = [clip.set_end(max_clip_duration) if float(clip.duration) > max_clip_duration else clip for clip in video_file_clips]
        # compute duration of video
        duration = sum([float(clip.duration) for clip in video_file_clips])
        print(f"({iteration}) Found clips, {duration} seconds long")
        iteration += 1
    print("Found clips that are long enough.\nProceeding now.")
    # Put all clips together
    concatenated_videoclip: VideoClip = concatenate_videoclips(video_file_clips)

    # Cap video duration to length of voiceover
    concatenated_videoclip = concatenated_videoclip.set_duration(voice_duration)
    print(f"Duration of final video: {float(concatenated_videoclip.duration)} seconds")
    # Close VideoFileClips
    [clip.close() for clip in video_file_clips]

    # Add subtitles text to video
    generator = lambda txt: TextClip(txt, font=font, fontsize=font_size, color=text_color, stroke_color=stroke_color, stroke_width=stroke_width, align="center", size=concatenated_videoclip.size, method="caption", transparent=True)
    generator_glow = lambda txt: TextClip(txt, font=font, fontsize=font_size, color=text_color, align="center", size=concatenated_videoclip.size, method="caption", bg_color="black")

    sub = SubtitlesClip(subtitles_path, generator)
    sub_glow1 = SubtitlesClip(subtitles_path, generator_glow)
    sub_glow = sub_glow1.fl_image(lambda image: cv2.GaussianBlur(image, (2 * glow_spread - 1, 2 * glow_spread - 1), 0))

    return concatenated_videoclip, sub, sub_glow, voice_duration


def _make_frame(t: float, clip_directory: str, subtitles_path: str, voice_over_path: str, font: str, font_size: int, text_color: str, stroke_color: str, stroke_width: int,  glow_spread: int, num_clips: int, clip_duration: float):
    concatenated_videoclip, sub, sub_glow, subs_duration = _make_clips(clip_directory, subtitles_path, voice_over_path, font, font_size, text_color, stroke_color, stroke_width, glow_spread, num_clips, clip_duration)
    # Create a frame
    frame = cv2.add(concatenated_videoclip.get_frame(t), sub_glow.set_pos(('center','center')).get_frame(t))
    return frame


def write_video(clip_directory: str, subtitles_path: str, background_music_directory: str, voice_over_path: str, output_path: str, font: str, font_size: int, text_color: str, stroke_color: str, stroke_width: int,  glowing_text: bool, glow_spread: int, num_clips: int, clip_duration: float):
    
    concatenated_videoclip, sub, sub_glow, subs_duration = _make_clips(clip_directory, subtitles_path, voice_over_path, font, font_size, text_color, stroke_color, stroke_width, glow_spread, num_clips, clip_duration)
    if glowing_text: concatenated_videoclip = VideoClip(lambda t: _make_frame(t, clip_directory, subtitles_path, voice_over_path, font, font_size, text_color, stroke_color, stroke_width,  glow_spread), duration=subs_duration)

    final_video = CompositeVideoClip([concatenated_videoclip, sub], (1080, 1920)).volumex(0.0)

    voiceover: AudioClip = AudioFileClip(voice_over_path)
    bg_music: AudioClip = AudioFileClip(random.choice([os.path.join(background_music_directory, music) for music in os.listdir(background_music_directory)])).volumex(0.1).subclip(t_start=20)
    audio = CompositeAudioClip([voiceover, bg_music]).set_end(subs_duration)
    final_video = final_video.set_audio(audio)

    # Write video file
    final_video.write_videofile(output_path, fps=30)
