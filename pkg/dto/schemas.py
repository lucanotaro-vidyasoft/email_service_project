from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Dict, Optional

class EmailTypeEnum(str, Enum):
    RESERVE = "RESERVE"
    RETURN = "RETURN"

class EmailRequest(BaseModel):
    emailType: EmailTypeEnum
    
    recipient_email: EmailStr
    metadata: Dict[str, str] = {}

class EmailResponse(BaseModel):
    success: bool
    message: str