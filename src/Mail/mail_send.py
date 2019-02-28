import smtplib

c=open('credentials','r')
c_line=c.readlines()
id=c_line[0]
pas=c_line[1]
message= ' '
b=open('body','r')
b_line=b.readlines()
for i in range(0,b_line.__len__()):
    message+=b_line[i]
print(message)

s = smtplib.SMTP('smtp.gmail.com:587')
s.ehlo()
# start TLS for security
s.starttls()


s.login(id,pas)


#message = "hie mpp this is dhiren sendig using lilly"


s.sendmail(id, "patelmp815@gmail.com", message)
print('mail sent')

s.quit()