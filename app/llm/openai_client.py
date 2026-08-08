from openai import OpenAI

from .base import BaseLLM

from pydantic import BaseModel

from app.core.config import get_settings
from .utils import parse_json

settings = get_settings()



class OpenAIClient(BaseLLM):

    def __init__(self):
        self.client = OpenAI(

            api_key=settings.OPENAI_API_KEY,

            base_url=settings.OPENAI_BASE_URL
            )

        self.model=settings.OPENAI_MODEL

    def chat(
                self,
                messages,
                response_model: type[BaseModel] | None = None
        ):
    
            if response_model is None:
    
                response = self.client.chat.completions.create(
                            model=self.model,
                
                            messages=messages,
                            
                            temperature=0.7,
                        )
                
                return response.choices[0].message.content
    
            completion = self.client.chat.completions.parse(
    
                model=self.model,
    
                messages=messages,
    
                response_format=response_model
            )
    
            messages = completion.choices[0].message
    
            if messages.refusal:
                raise Exception(f"Refusal: {messages.refusal.reason}")
    
            if messages.parsed is None:
                raise Exception(f"Failed to parse response: {messages.content}")
    
            return messages.parsed

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