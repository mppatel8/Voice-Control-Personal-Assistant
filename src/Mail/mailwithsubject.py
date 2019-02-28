import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from speak import pyspeak

def sendmail():
    message=' '
    b=open('body','r')
    b_line=b.readlines()
    for i in range(0,b_line.__len__()):
        message+=b_line[i]
    c=open('credentials','r')
    c_line=c.readlines()
    id=c_line[0]
    password=c_line[1]
    d=open('recipient','r')
    d_line=d.readlines()
    rec=d_line[0]
    e=open('subject', 'r')
    e_line=e.readlines()
    sub=e_line[0]
    
    #fromaddr = "dhiren905@gmail.com"
    #toaddr = "patelmp815@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = id
    msg['To'] = rec
    msg['Subject'] = sub
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(id, password)
    text = msg.as_string()
    server.sendmail(id, rec, text)
    text1="mail sent successfully bro!!!!!"
    print(text1)
    pyspeak.speakup(text1)