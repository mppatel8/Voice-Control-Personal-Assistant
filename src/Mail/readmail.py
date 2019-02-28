import imaplib
import email
from speak import speech
from speak import pyspeak
from bs4 import BeautifulSoup
import re

c=open('credentials','r')
c_line=c.readlines()
id=c_line[0]
password=c_line[1]


count=1  

try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(id,password)
        mail.select('inbox')
        
        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids.split()

        for i in reversed(id_list):
            if count<=1:
                typ, data = mail.fetch(i, '(RFC822)' )

                for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_string(response_part[1].decode('utf-8'))
                        email_subject = msg['subject']
                        email_from = msg['from']
                        
                       # if msg.is_multipart():
                        #    for payload in msg.get_payload():
                         #       # if payload.is_multipart(): ...
                          #      email_body=payload.get_payload()
                           #     print (email_body)
                        #else:
                        email_body=msg.get_payload()
                          #  print (email_body)
                        #email_body=msg.get_payload()
                        #t = re.sub(r'\<[^>]*\>', '', email_body)
                        #soup=BeautifulSoup(str(email_body),"html.parser")
                        #b=html2text(email_body, ignore_tags=("img"), indent_width=4, page_width=80)
                        #email_body=soup.get_text()
                        #p=email_body.encode("utf-8")
                        #body=soup.get_text()
                        #t = re.sub(r'\[[^>]*\]', '', body)
                        text='Mail Number' + str(count) +'From : ' + email_from + 'Subject : ' + email_subject + 'Message is:' 
                        print('Mail Number' + str(count) + '\n\nFrom : ' + email_from + '\n')
                        print('Subject : ' + email_subject + '\n')
                        print('Message is'+'\n')
                        print(email_body)
                        pyspeak.speakup(text)
                
                        count=count+1

except Exception as e:
                        print(str(e))
    