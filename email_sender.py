from email.message import EmailMessage
import smtplib
from string import Template
# from pathlib import Path
from config import config


class EmailSender:
    data = {"name": "Unknown", "email": "Unknown", "message": ""}

    def __init__(self, data: dict):
        self.data = data
        mail = EmailMessage()
        mail["from"] = config.sender
        mail["To"] = config.recipient
        try:
            mail["subject"] = f"{data["email"]}'s message"
            # mail.set_content(html.substitute({"name": "Peter"}), "html")
            mail.set_content(f"{data["name"]} has sent you a message through portfolio website:\n"
                             f"{data["message"]}")

            with smtplib.SMTP(host=config.host, port=587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(config.sender, config.sender_password)
                smtp.send_message(mail)
                print("Msg sent!")

        except:
            print("sg went wrong")
    # html = Template(open("index.html").read())

