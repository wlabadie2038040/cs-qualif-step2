from pydantic import BaseModel

class RegisterDeviceRequest(BaseModel):
    macAddress: str
    model: str
    firmwareVersion: str
    serialNumber: str
    displayName: str
    location: str
    timezone: str
