import smtplib
import ssl


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from string import Template
from el import email_reciever


email_senders = {
    "sdlkjflkdsj@gmail.com": "password1",
    "slkdjflksjdf@gmail.com": "password2",
    "slkdjlkdsjijei@gmail.com": "password3",
}


html = Template((Path(__file__).parent / "index.html").read_text())

message = MIMEMultipart("alternative")


for email_sender, email_password in email_senders:
    message["Subject"] = "Crypto"
    message["From"] = email_sender
    message["To"] = email_reciever

    part = MIMEText(
        html.substitute(
            {
                "btc_value": 25563,
            }
        ),
        "html",
    )
    message.attach(part)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        print("Connecting to server...")
        server.login(email_sender, email_password)
        print("Logging...")
        server.sendmail(email_sender, email_reciever, message.as_string())
        print("Email was sent!")
