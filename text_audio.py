import speech_recognition as sr
recognizer =sr.Recognizer()

from io import BytesIO
from pydub import AudioSegment
from pydub.playback import  play
from gtts import gTTS
import json, os, shutil, random, subprocess
from PIL import Image
from pydub import AudioSegment
import ffmpeg
def txt_aud(text):
    language ='en'
    tts= gTTS(text=text,lang=language)
    mp3_fp=BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    audio=AudioSegment.from_file(mp3_fp,format='mp3')
    play(audio)

txt_aud("attulaya")
