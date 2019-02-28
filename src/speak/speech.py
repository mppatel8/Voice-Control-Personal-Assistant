from gtts import gTTS
from googletrans import Translator

import os


def speak(text):
    tts = gTTS(text=text,lang='en-uk')
    tts.save("good.mp3")
    os.system("good.mp3")
def translation(text):
    t= Translator()
    tr=t.translate(text,dest='hi')
    return tr.text
def speakhindi(text):
    tts =gTTS(text=text,lang='hi')
    tts.save('good.mp3')
    os.system('good.mp3')
