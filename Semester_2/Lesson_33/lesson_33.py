import smtplib, ssl
import re


from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from practice.el import email_reciever


with open("data1.csv", "r", encoding="utf-8") as file:
    d = []
    for r in file.readlines():
        d.append(" | ".join((re.split(r"[\n,;]", r))) + "<br>")
    d.insert(1, len(d[1]) * "_" + "<br>")


text = "".join(d)

html = f"""\
<html>
    <body style="font-family:monospace;">
        <h2 style="color:red;">Users and passwords</h2>
        <h3 style="margin:10px auto 0px auto;background-color:green;color:#FFFFFF;padding:20px;box-shadow:2px 2px 12px gray;">
            {text}
        </h3>
    </body>
</html>
"""

email_sender_list = {
    "sdlkjflkdsj@gmail.com": "password1",
    "slkdjflksjdf@gmail.com": "password2",
    "slkdjlkdsjijei@gmail.com": "password3",
}

port = 465  # For SSL

message = MIMEMultipart("alternative")


for email, password in email_sender_list.items():
    message["Subject"] = "multipart test"
    message["From"] = email
    message["To"] = email_reciever

    sender_email = email
    password = password
    reciever_email = email_reciever

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()

    print("Sending email...")
    with smtplib.SMTP_SSL("smtp.gmail.com", port=port, context=context) as server:
        server.login(sender_email, password)
        print("Logged in...")

        server.sendmail(sender_email, reciever_email, message.as_string())
        print("Email was sent!")
