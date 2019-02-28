from music import musics

f=open('inupt','r')
lines=f.readlines()
print(lines)
song=lines[0]+'.mp3'

musics.music_play(song)

