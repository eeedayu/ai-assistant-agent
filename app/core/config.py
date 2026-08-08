from functools import lru_cache

from pydantic_settings import BaseSettings      


class Settings(BaseSettings):

    DEFAULT_PROVIDER: str = "deepseek"

    ########################################

    OPENAI_API_KEY: str = ""

    OPENAI_BASE_URL: str = "https://api.openai.com/v1"

    OPENAI_MODEL: str = "gpt-4.1-mini"

    ########################################

    DEEPSEEK_API_KEY: str = ""

    DEEPSEEK_BASE_URL: str = "https://api.deepseek.com/v1"


    DEEPSEEK_MODEL: str = "deepseek-v4-flash"

    ########################################

    OLLAMA_BASE_URL: str = "http://localhost:11434/v1"

    OLLAMA_MODEL: str = "qwen2.5:7b"

    class Config:
        env_file = ".env"
        extra = "ignore"

@lru_cache
def get_settings() -> Settings:
    return Settings()