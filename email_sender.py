from email.message import EmailMessage
import smtplib
from string import Template
# from pathlib import Path


class EmailSender:
    data = {"name": "Unknown", "email": "Unknown", "message": ""}

    def __init__(self, data: dict):
        self.data = data
        mail = EmailMessage()
        mail["from"] = "zerotomastery@freemail.hu"
        mail["To"] = "anonymous9832@gmail.com"
        try:
            mail["subject"] = f"{data["email"]}'s message"
            # mail.set_content(html.substitute({"name": "Peter"}), "html")
            mail.set_content(f"{data["name"]} has sent you a message through portfolio website:\n"
                             f"{data["message"]}")

            with smtplib.SMTP(host="smtp.freemail.hu", port=587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login("zerotomastery@freemail.hu", "Eztigynem01")
                smtp.send_message(mail)
                print("Msg sent!")

        except:
            print("sg went wrong")
    # html = Template(open("index.html").read())

