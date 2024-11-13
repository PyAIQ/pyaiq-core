from fastapi import APIRouter, HTTPException

from handler import handle_init
from core import event_handlers

on_init_router = APIRouter()


@on_init_router.post("/on_init")
async def on_init_ep(data: dict):
    if 'on_init' in event_handlers:
        result = event_handlers['on_init'](data)
        return result
    raise HTTPException(status_code=404, detail="on_init handler not found")
