import wikipedia
import re
from speak import pyspeak

def searchtopic():
    f=open('topicinput', 'r')
    t=f.readlines()
    try:
        o=wikipedia.summary(t, sentences=5)
        t=re.sub(r'\([^)]*\)', '', o)
    
        p=t.encode("utf-8")
        print(p)
    
        pyspeak.speakup(p)
    
    except Exception as e:
             print(str(e))
             pyspeak.speakup(e)
             print("----------")
    