from ww import weaterinfo as we

def weather():
    d=open('location','r')
    d_line=d.readlines()
    rec=d_line[0]
        
    w= we.weather_info(rec)




#import os
#os.system("espeak 'hello there i am gideon'")