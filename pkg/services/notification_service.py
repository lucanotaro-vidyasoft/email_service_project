from pkg.dto.schemas import EmailRequest
from pkg.utils.smtp_client import SmtpClient
from pkg.templates import EMAIL_TEMPLATES

class NotificationService:
    def __init__(self):
        self.smtp_client = SmtpClient()

    def process_request(self, request: EmailRequest):

        template_func = EMAIL_TEMPLATES.get(request.emailType)

        if not template_func:
            raise ValueError(f"Template non trovato per: {request.emailType}")

        subject, body = template_func(request.metadata)

        success = self.smtp_client.send(
            to_email=request.recipient_email,
            subject=subject,
            body=body
        )

        if not success:
            raise Exception("ATTENZIONE MAIL NON INVIATA")
        
        return success