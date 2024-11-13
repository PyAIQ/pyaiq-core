import logging

from langchain_core.messages import AIMessage

from core import on_query
from llm_util import LlmBuilder


@on_query
def handle_query(data):
    logging.info(f"Server received on_query with data: {data}")
    ai_ = LlmBuilder().model()
    messages = [
        data['query']
    ]
    response = AIMessage(ai_.invoke(messages))
    return response.content

