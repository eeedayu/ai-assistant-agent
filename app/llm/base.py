from    abc import ABC, abstractmethod
from typing import Type
from pydantic import BaseModel

class BaseLLM(ABC):

    @abstractmethod
    def chat(
        self,
        messages: list,
        response_model: type[BaseModel] | None = None
    ):
        pass

    @abstractmethod
    def stream_chat(
        self,
        messages: list
    ):
        pass