import logging
import os

from middleware.llm_util.llm_provider import LLM_MODEL
from type import LlmServiceProvider
from type.Singleton import Singleton


class LlmBuilder(Singleton):
    def __init__(self):
        self.__model = self.__initialize_model()

    @staticmethod
    def __initialize_model():
        try:
            model_provider = LlmServiceProvider(os.getenv('LLM_SERVICE_PROVIDER'))
            return LLM_MODEL[model_provider]().instance()
        except Exception as e:
            logging.error(e)
            raise e

    def model(self):
        return self.__model
