from app.llm.factory import LLMFactory
from app.prompts.manager import PromptManager
from app.schemas.resume import ResumeInfo

class ChatService:
    def __init__(self, provider="deepseek"):
        self.llm = LLMFactory.create(provider)

    def chat(self, question: str, history=None):
        messages = PromptManager.build_chat_messages(
            question=question,
            history=history
        )
        return self.llm.chat(messages)

    def stream(self, question: str, history=None):
        messages = PromptManager.build_chat_messages(
            question=question,
            history=history
        )
        return self.llm.stream_chat(messages)