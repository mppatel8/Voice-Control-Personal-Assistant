import sounddevice as sd
from speak import pyspeak

myrec=sd.rec()
print(myrec)
pyspeak.speakup(myrec)
