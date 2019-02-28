from pygame import *


##for stop  mixer.stop()  for pause mixer.pause() for unpause mixer.unpause()
def music_play(song):
    mixer.init()
    mixer.music.load(song)
    mixer.music.play()

    while mixer.music.get_busy():
        time.Clock().tick(10)

def music_stop():
    mixer.stop()

def music_pause():
    mixer.pause()

def music_unpause():
    mixer.unpause()