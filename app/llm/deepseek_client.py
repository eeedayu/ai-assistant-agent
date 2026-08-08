from openai import OpenAI

from .base import BaseLLM

from pydantic import BaseModel

from app.core.config import get_settings
from .utils import parse_json

settings = get_settings()



class DeepSeekClient(BaseLLM):

    def __init__(self):
        self.client = OpenAI(

            api_key=settings.DEEPSEEK_API_KEY,

            base_url=settings.DEEPSEEK_BASE_URL
            )

        self.model=settings.DEEPSEEK_MODEL

    def chat(

        self,

        messages,

        response_model: type[BaseModel] | None = None,

    ):

        response = self.client.chat.completions.create(

            model=self.model,

            messages=messages,

            temperature=0.7,

        )

        content = response.choices[0].message.content

        if response_model is None:

            return content

        data = parse_json(content)

        return response_model.model_validate(data)

    def stream_chat(
            self,
            messages
    ):
        stream = self.client.chat.completions.create(
            model=self.model,

            messages=messages,
            
            temperature=0.7,

            stream=True
        )

        for chunk in stream:

            if not chunk.choices[0].delta:
                continue

            delta = chunk.choices[0].delta

            if delta.content:
                yield delta.content