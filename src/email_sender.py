import smtplib
from email.message import EmailMessage

class NewClient:

    def login_client(self, email : str, password : str):
        self.email = email
        self.password = password
        self.smtp = smtplib.SMTP(host = "smtp.gmail.com", port = 587)
        self.smtp.ehlo()
        self.smtp.starttls()
        try:
            self.smtp.login(email, password)
            print("Logged in successfully!")
            return 1
        except Exception:
            print("Invalid credentials, or SMTP not enabled!")
            return 0

    def new_message(self, email_from : str, email_to : str, email_subject : str, email_content : str):
        email = EmailMessage()
        email["from"] = email_from
        email["to"] = email_to
        email["subject"] = email_subject
        email.set_content(email_content)
        try:
            self.smtp.send_message(email)
            print("Sent!")
            return 1
        except Exception:
            return 0

