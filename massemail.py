#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 09:14:44 2018

@author: shrutikapatil
"""

#Import the smtplot library in python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
# Upgrade the connection to a secure one using TLS (587)
smtpObj.starttls()
# To start the connection
smtpObj.ehlo() 

#login with your email id and password
smtpObj.login('my_email@gmail.com', 'my_password')

#lists
clist = 'Wipro', 'GHD','Disney' #list of companies
nlist = 'Sidharth', 'Eric', 'Thomas' #list of company representatives
elist = 'jasrasidhrath@gmail.com', 'eric123@gmail.com', 'Thomas123@gmail.com' #list of email ids of representatives

#Iterate the forloop to send  email to each company representative.
for i in range(0, len(elist)):
    msg = MIMEMultipart()
    msg['From'] = 'Sidharth Jasra <jasrasidharth@gmail.com>'
    msg['To'] = '%s <' % nlist[i] +elist[i] + '>'
    msg['Subject'] = 'Thank you for attending our conference and sharing your views on work life at %s' % clist[i]
    
    #email file attachment
    filename='Gift_Card.pdf'
    fp=open(filename,'rb')
    att = MIMEApplication(fp.read(),_subtype="pdf")
    att.add_header('Content-Disposition','attachment',filename=filename)
    msg.attach(att)

    #Email template
    message = 'Hi %s,\n\nHope you are doing well!\n\n\
    It is really nice to meet you at the conference last evening.\
    The thoughts you have shared with audience about the work culture at %s was really helpful for me.\
    Thank you so much for valuable insights about the company.\
    I am attaching a gift card for you.\n\n\n- Sidharth' % (nlist[i], clist[i])
    msg.attach(MIMEText(message))
    smtpObj.sendmail('jasrasidharth@gmail.com',elist[i],msg.as_string())
smtpObj.quit()
