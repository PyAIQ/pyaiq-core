import logging

from core import on_init
from llm_util import LlmBuilder


@on_init
def handle_init(data):
    logging.info(f"Server received on_init with data: {data}")
    LlmBuilder()
    return {"status": "init completed"}
