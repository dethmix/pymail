#!/usr/bin/python

import smtplib
import socket

sender = 'sender@domain.com'
recipient = 'recipient@domain.com'

message = """From: <sender@domain.com>
To: <recipient@domain.com>
Subject: html based email message
MIME-Version: 1.0
Content-type: text/html

<h1> large header </h1>
"""

try:
	smtpObj = smtplib.SMTP('localhost')
	smtpObj.sendmail(sender, recipient, message)
	print 'Message was sent'
except smtplib.SMTPException:
	print "ERROR: message was NOT sent"
except socket.error:
	print "ERROR: wasn't able to establish connection to the host"
