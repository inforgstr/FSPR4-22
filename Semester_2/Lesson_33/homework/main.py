import os
import smtplib
import ssl


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from string import Template


email_sender = os.environ.get("email")
email_password = os.environ.get("email_password")

recievers = [
    "example@example.com",
    "example@example.com",
]

html = Template((Path(__file__).parent / "index.html").read_text())

message = MIMEMultipart("alternative")

part = MIMEText(
        html.substitute(
            {
                "btc_value": 25563,
            }
        ),
        "html",
    )
message.attach(part)

message["Subject"] = "Crypto"
message["From"] = email_sender


for email_reciever in recievers:
    message["To"] = email_reciever

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        print("Connecting to server...")
        server.login(email_sender, email_password)
        print("Logging...")
        server.sendmail(email_sender, email_reciever, message.as_string())
        print(f"Email was sent to {email_reciever}!\n")
