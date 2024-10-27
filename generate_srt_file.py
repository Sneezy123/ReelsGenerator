import whisper
import os
from math import ceil


# I know that there is a srt file generator method from whisper but I have my settings here as I want them.

def hhmmss_from_sec(sec: float):
    hh = sec // 3600 # How many hours are in the seconds (3600 seconds for one hour)
    mm = sec % 3600 // 60 # How many minutes are in the remaining seconds
    ss = sec % 60 # How many seconds are in the remaining seconds
    ms = int((ss % 1) * 1000) # How many milliseconds are in the remaining seconds
    return f"{int(hh):02d}:{int(mm):02d}:{int(ss):02d},{ms:03d}"


# https://www.30secondsofcode.org/python/s/chunk-list/
def chunk(lst, size):
  return list(
    map(lambda x: lst[x * size:x * size + size],
      list(range(ceil(len(lst) / size)))))



def generate_srt(audio_file_path: str = "voiceover.mp3",  output_file_path: str = "subtitles.srt", chunk_size: int = 3, verbose = bool | None):
    model = whisper.load_model("small.en")

    result = model.transcribe(audio_file_path, verbose=verbose, word_timestamps=True)
    srt_file_name: str = os.path.split(output_file_path)[-1]

    segments = result['segments']

    with open(srt_file_name, "w") as f:
        f.write("")

    with open(srt_file_name, 'a', encoding='utf-8') as srtFile:
        word_cluster_text: str = ""
        id = 1
        for seg in segments:
            word_clusters = chunk(seg["words"], chunk_size)
            for word_cluster in word_clusters:
                start = hhmmss_from_sec(word_cluster[0]["start"])
                end = hhmmss_from_sec(word_cluster[-1]["end"])
                for word in word_cluster:
                    word_cluster_text += word["word"]
                segment = f"{id}\n{start} --> {end}\n{word_cluster_text.strip()}\n\n"
                word_cluster_text = ""
                id += 1
                srtFile.write(segment)
