import PyPDF2
#from speak import pyspeak as p
import os

#from speak import speech
i=0

file = open('170701.pdf','rb')

reader = PyPDF2.PdfFileReader(file)

pgno=reader.getNumPages()
print(pgno)

while i<pgno:
    page = reader.getPage(i)
    page_text = page.extractText()
    print(page_text)
    #speech.speak(page_text)
    #p.speakup(page_text)
    i=i+1

