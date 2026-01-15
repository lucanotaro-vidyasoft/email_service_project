import os

class SmtpSettings:
    
    HOST = "sandbox.smtp.mailtrap.io"
    PORT = 2525
    
    USER = os.getenv("SMTP_USER", "")
    PASSWORD = os.getenv("SMTP_PASSWORD", "")
    
    SENDER_EMAIL = "Private Person <from@example.com>"