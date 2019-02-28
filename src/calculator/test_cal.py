from speak import speech as s
from calculator import operations as op
from speak import pyspeak as ps

#a=[10,20]
r=open('second_input','r')
li=r.readlines()
for l in li:
    id=l.split(" ",-1)
    
    print(id)
    print("_______")
   
    

#ans1=op.add(a)
#ans2=op.sub(a)
#ans3=op.div(a)
#area=op.area_circle(a[0])
#text='the addition of %d and %d is %d '%(a[0],a[1],ans1)
#text1='the subtraction of %d  and %d is %d'%(a[0],a[1],ans2)
#text2="the area of circle with radius %d is %d"%(a[0],area)
#s.speak(text+text1)
#s.speak(text2)
#ps.speakup(text+" "+text1+" "+text2)