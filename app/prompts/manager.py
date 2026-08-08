from .system import SYSTEM_PROMPTS

from .templates import CHAT_TEMPLATE, SUMMARIZE_TEMPLATE, REWRITE_TEMPLATE, RESUME_TEMPLATE


example_messages = [

{
    "role":"user",
    "content":"你好"
},

{
    "role":"assistant",
    "content":"你好，请问有什么可以帮助你？"
}
]

class PromptManager:

    @staticmethod
    def build_chat_messages(
        question: str,
        history: list | None = None,
        role="assistant"
    ):
        history = history or []

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPTS[role]
            }
        ]

        messages.extend(example_messages)

        messages.extend(history)

        messages.append(
            {
                "role": "user",
                "content": CHAT_TEMPLATE.format(
                    question=question
                )
            }
        )
        return messages

    @staticmethod
    def build_resume_messages(
        text: str
    ):

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPTS["resume"]
            }
        ]

        messages.append(
            {
                "role": "user",
                "content": RESUME_TEMPLATE.format(text=text)
            }
        )
        return messages