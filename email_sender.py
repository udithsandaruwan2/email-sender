from email.message import EmailMessage
import ssl
import smtplib

#sender Credentials
email_sender = "senders_email"
email_password = "senders_secret_password"

email_receiver = input("Enter Receiver's Email : ")

email_subject = input("Subject : ")

email_body = input("Message : \n")

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = email_subject
em.set_content(email_body)

#set the context
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

print("Email sent successfully!")