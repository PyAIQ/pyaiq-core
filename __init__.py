from fastapi import FastAPI

from api import on_query_router, on_close_router, on_init_router
from ws import ws_router


app = FastAPI()
app.include_router(on_init_router)
app.include_router(on_close_router)
app.include_router(on_query_router)
app.include_router(ws_router)
