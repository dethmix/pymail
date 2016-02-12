#!/usr/bin/python

import smtplib

send = 'sender@domain.com'
recipient = 'recipient@domain.com'

message = """From: <sender@domain.com>
To: <recipient@domain.com>
Subject: 'Hello pymail'


Test message from the python script
"""

smtpObj=smtplib.SMTP('localhost')
smtpObj.sendmail(send, recipient, message)


