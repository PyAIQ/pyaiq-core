from fastapi import APIRouter, HTTPException

from handler import handle_query
from core import event_handlers

on_query_router = APIRouter()


@on_query_router.post("/on_query")
async def on_query_ep(query: dict):
    if 'on_query' in event_handlers:
        result = event_handlers['on_query'](query.get("query", ""))
        return result
    raise HTTPException(status_code=404, detail="on_query handler not found")
