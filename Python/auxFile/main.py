from gtts import gTTS
#pip install gtts
from playsound import playsound
# pip install playsound

audio = 'speech.mp3'
language = "en"
sp = gTTS(text="Follow my github account x33lyS", lang=language)
sp.save(audio)
playsound(audio)