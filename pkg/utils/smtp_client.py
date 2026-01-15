import smtplib
from pkg.config.settings import SmtpSettings

class SmtpClient:
    
    def send(self, to_email: str, subject: str, body: str) -> bool:

        sender = SmtpSettings.SENDER_EMAIL
        receiver = to_email

        message = f"""\
Subject: {subject}
To: {receiver}
From: {sender}

{body}"""

        try:
            with smtplib.SMTP(SmtpSettings.HOST, SmtpSettings.PORT) as server:
                server.starttls()
                server.login(SmtpSettings.USER, SmtpSettings.PASSWORD)
                
                server.sendmail(sender, receiver, message.encode("utf-8"))
            
            return True

        except Exception as e:

            print(f"ERRORE SMTP SANDBOX: {e}")
            return False