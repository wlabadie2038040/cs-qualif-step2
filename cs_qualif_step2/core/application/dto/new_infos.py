from dataclasses import dataclass

@dataclass
class NewInfos:
    firmwareVersion: str
    displayName: str
    location: str
    timezone: str