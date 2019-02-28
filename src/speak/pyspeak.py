import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate',100)
engine.setProperty('volume',0.9)

def speakup(text):
    engine.say(text)
    engine.runAndWait()


#import os
#os.system("espeak 'hello there i am gideon'")