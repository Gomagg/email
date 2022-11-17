from email.message import EmailMessage
from apcont import password
import ssl
import smtplib

email_sender = 'emmanueloluwagbemi99@gmail.com'
email_password = password

email_receiver = 'adeyeyeemmanuel6@gmail.com'

subject = "Don't forget to subscribe"
body = """
Thank you for checking in, please subscribe for future sales.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    
