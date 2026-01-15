from fastapi import APIRouter, HTTPException, status
from pkg.dto.schemas import EmailRequest, EmailResponse
from pkg.services.notification_service import NotificationService

router = APIRouter(prefix="/api/internal/emails")
service = NotificationService()

@router.post("/send/v1", response_model=EmailResponse)
def send_email_endpoint(payload: EmailRequest):
    try:
        service.process_request(payload)
        
        return EmailResponse(
            success=True, 
            message="Email inviata correttamente, lesgoski!"
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )