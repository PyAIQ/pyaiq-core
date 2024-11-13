from enum import StrEnum


class LlmServiceProvider(StrEnum):
    OPEN_AI = 'open_ai'
    AZURE = 'azure'
    GOOGLE = 'google'
