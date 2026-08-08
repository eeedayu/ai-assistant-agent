from   typing import Type

from   pydantic import BaseModel


from app.llm.base import BaseLLM
from app.prompts.manager import PromptManager
from app.schemas.resume import ResumeInfo

class ExtractService:

    def __init__(self, llm: BaseLLM):
        self.llm = llm

    def extract_resume(
        self,
        text: str,
        history=None
    )-> ResumeInfo:
        messages = PromptManager.build_resume_messages(
            text=text,
            history=history
        )
        return self.llm.chat(messages, response_model=ResumeInfo)