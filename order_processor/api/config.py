from functools import lru_cache
from pydantic import BaseSettings, Field


class Settings(BaseSettings):

    API_NAME: str = Field('Order processor', description='Nome da API')


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
