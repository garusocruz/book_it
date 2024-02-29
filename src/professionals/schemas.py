from datetime import datetime
from pydantic import BaseModel



class ProfessionalBase(BaseModel):
    customer_id: int
    expertise: str


class ProfessionalCreate(ProfessionalBase):
    created_at: datetime = datetime.now()
    updated_at: datetime | None = None
    

class  Professional(ProfessionalBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True
