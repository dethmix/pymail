#!/usr/bin/python

import smtplib

send = 'dmitriy.pavlov@ecommerce.com'
recipient = 'dethmix@gmail.com'

message = """From: <dmitriy.pavlov@ecommerce.com>
To: <dethmix@gmail.com>
Subject: 'Hello pymail'


Test message from the python script
"""

smtpObj=smtplib.SMTP('localhost')
smtpObj.sendmail(send, recipient, message)


