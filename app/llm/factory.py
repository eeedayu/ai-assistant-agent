from .deepseek_client import DeepSeekClient

from .openai_client import OpenAIClient

from app.core.config import get_settings



class LLMFactory:

    @staticmethod
    def create(
        provider=None
    ):
        settings = get_settings()

        provider = provider or settings.DEFAULT_PROVIDER

        provider = provider.lower()

        if provider == "deepseek":
            return DeepSeekClient()
        elif provider == "openai":
            return OpenAIClient()
        else:
            raise Exception(f"Unsupported provider: {provider}")