#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText

sender = 'sender@domain.com'
recipient = 'recipient@domain.com'
subject = 'pymail mime message'
message = '''Hello, really nice message from python'''

msg = MIMEText(message)
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = subject

mail = smtplib.SMTP('localhost')
mail.sendmail(sender, recipient, msg.as_string())
mail.quit()
