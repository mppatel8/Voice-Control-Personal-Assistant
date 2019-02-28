from speak import pyspeak
from Mail import mailwithsubject
from Mail.mailwithsubject import sendmail
from topic_search import topic
from topic_search.topic import searchtopic
from speak import pyspeak
from ww.test_weather import weather

r=open('messageinput','r')
li=r.readlines()
for l in li:
    id=l.split(" ",-1)    
# print(id)
    
with open('levelone', 'rU') as in_file:
    data = in_file.read().split('\n')
# print(data)
data1=dict()
z=-1
k=0
key=''
for i in id:
    print(i)
    for j in data:
        print(j)
        
        k=k+1
        if i==j:
            print("match found at "+i+" "+j )
            key=data[k-1]
            z=k-1
    k=0
print(key)

if z==-1:
    pyspeak.speakup("speak properly")

#if z==0 or z==1 or z==2 or z==3:
    
if z==4 or z==5 or z==6:
    searchtopic()

if z==7:
    weather()

if z==8:
    sendmail()    
