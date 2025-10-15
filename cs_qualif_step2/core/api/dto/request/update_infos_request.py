from pydantic import BaseModel, validator

class UpdateInfosRequest(BaseModel):
    firmwareVersion: str
    displayName: str
    location: str
    timezone: str

    @validator('firmwareVersion')
    def not_empty(cls, v):
        if v is None or v.strip() == '':
            raise ValueError('Field cannot be empty or null')
        return v
