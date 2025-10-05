from http.client import HTTPResponse

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

device_router = APIRouter(
    prefix="/api/v1/devices",
    tags=["devices"]
)


@device_router.post("")
def register_device():
    return JSONResponse(
        code=status.HTTP_201_CREATED
    )
