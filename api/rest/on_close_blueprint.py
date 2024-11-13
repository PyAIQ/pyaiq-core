from fastapi import APIRouter, HTTPException

from handler import handle_close
from core import event_handlers

on_close_router = APIRouter()


@on_close_router.post("/on_close")
async def on_close_ep(data: dict):
    if 'on_close' in event_handlers:
        result = event_handlers['on_close'](data)
        return result
    raise HTTPException(status_code=404, detail="on_close handler not found")
