from Mail import mail_send as m

cre=open('credentials','r')
c_lines=cre.readlines()
idsender=c_lines[0]
pas=c_lines[1]


bo=open('body','r')
b_line=bo.readlines()
message=' '
for i in range(0,b_line.__len__()):
    message+=b_line[i]

m.sendmail(idsender,pas,'arunaj666@gmail.com',message)