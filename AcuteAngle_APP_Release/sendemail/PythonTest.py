#! /usr/bin/python 
# -*- coding: utf-8 -*-

import sys
import os
import SendMailModule
if len(sys.argv) == 2:
   attachmentfile1 = sys.argv[1]
   attachments=[attachmentfile1]
elif len(sys.argv) == 3:
   attachmentfile1 = sys.argv[1]
   attachmentfile2 = sys.argv[2]
   attachments=[attachmentfile1,attachmentfile2]
elif len(sys.argv) == 4:
   attachmentfile1 = sys.argv[1]
   attachmentfile2 = sys.argv[2]
   attachmentfile3 = sys.argv[3]
   attachments=[attachmentfile1,attachmentfile2,attachmentfile3]
elif len(sys.argv) == 5:
   attachmentfile1 = sys.argv[1]
   attachmentfile2 = sys.argv[2]
   attachmentfile3 = sys.argv[3]
   attachmentfile4 = sys.argv[4]
   attachments=[attachmentfile1,attachmentfile2,attachmentfile3,attachmentfile4]
else:
   attachments=[]

mailHeader={ 'from' : 'integration@acuteangle.cn' , 'to' : 'test@acuteangle.cn' ,'cc' : 'cc@acuteangle.cn','bcc' :'','subject' : 'email test' }
para={'usr':'integration@acuteangle.cn','passwd':'sjx1234','server':'smtp.ym.163.com','body':''}

# Create receiver list
receivers=[] # receive mail persons
mailer='' # send mail person
for key,val in mailHeader.items():
    if val and (key.lower()=='to' or key.lower()=='cc' or key.lower()=='bcc'):
        receivers.extend(val.split(','))
    elif key.lower()=='from':
        mailer=val
    
print receivers
print mailer

# read mail data
piece1='''<p><font size="3">Dear all,<br></br>emailboby</font></p><br></br>'''
piece2='''<p><br><font size="2">Thanks!</font></br></p>'''


if not os.path.isfile("./str_no_trans.txt"):
    mailBody =[('html',piece1),('html',piece2)]
else:
    mailBody =[('html',piece1),('html',piece2)]

if para['body']:
    f=open(para['body'],'r')
    cList=f.readlines()
    f.close()

# Create mail
mail=SendMailModule.createMail(mailHeader,mailBody,attachments)
SendMailModule.sendMail(receivers,mailer,mail)
