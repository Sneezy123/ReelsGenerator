# ReelsGenerator
## by Sneezy123

> **Information**
> 
> This project generates videos with automatic captioning and AI voiceover with background music. The videos have the resolution of 1080x1920 (9:16), ideal for short videos like on TikTok, Instagram and YouTube, thus the name.

# Installation
> [!IMPORTANT]
> You need an API key for ElevenLabs (https://elevenlabs.io/docs/introduction) for this to work!

The project uses a couple of python packages to work. It also uses the ElevenLabs API for which you need an API key

First, clone this repository

Navigate to where the project should be saved

Open a command prompt and with git installed, run

```ps
git clone "https://github.com/Sneezy123/ReelsGenerator.git"
```


Alternatively, you could download the project and extract the content at the desired location

<img src="https://i.imgur.com/3RycDUN.png" width="50%">

When you have the project on you local machine, go to the project directory, open a command prompt and with python installed, run
```ps
pip install -r requirements.txt
```
or with Python 3
```ps
pip3 install -r requirements.txt
```

put your API key into the `.env` file (rename `.env.example` to `.env`) so that everything works

# Usage
You can start now!

put your clips, music into the input directory
change the prompt to what you want

Then go into the file `main.py` and change the different paths to your corresponding paths.

Run `main.py`
```ps
python main.py
```
or
```ps
python3 main.py
```
Enjoy!



