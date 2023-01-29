"""
import smtplib

# sender's email and password
sender_email = "incisltd@gmail.com"
sender_password = "123456"

# recipient's email
recipient_email = "mniniro@hotmail.com"

# email subject and message
subject = "Test email from Python"
message = "This is a test message sent from Python."

# setup the email
email = f"Subject: {subject}\n\n{message}"

# send the email
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.ehlo()  # start the connection
    server.starttls()  # secure the connection
    server.login(sender_email, sender_password)  # login
    server.sendmail(sender_email, recipient_email, email)  # send the email
"""

# ==============================================

import smtplib as smtp

sender_email = "sender@example.com"
receiver_email = "receiver@example.com"
password = "password"

message = """\
Subject: Test Email

This is a test email sent using Python."""

with smtp.SMTP("smtp.gmail.com", 587) as server:
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

