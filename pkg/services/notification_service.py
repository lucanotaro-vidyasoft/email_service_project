from pkg.dto.schemas import EmailRequest, EmailTypeEnum
from pkg.utils.smtp_client import SmtpClient

class NotificationService:
    def __init__(self):
        self.smtp_client = SmtpClient()

    def process_request(self, request: EmailRequest):
        user_name = request.metadata.get("user_name", "Utente non registrato :( ")
        book_title = request.metadata.get("book_title", "Libro non registrato :( ")
        
        subject = ""
        body = ""

        if request.emailType == EmailTypeEnum.RESERVE:
            subject = "Conferma Prenotazione"
            body = (
                f"Ciao {user_name},\n"
                f"Hai prenotato: {book_title}.\n"
                f"Questa è una test mail"
            )
            
        elif request.emailType == EmailTypeEnum.RETURN:
            subject = "Restituzione Avvenuta"
            body = (
                f"Ciao {user_name},\n"
                f"Hai restituito: {book_title}."
            )

        success = self.smtp_client.send(
            to_email=request.recipient_email,
            subject=subject,
            body=body
        )

        if not success:
            raise Exception("ATTENZIONE MAIL NON INVIATA")
        
        return success