from dotenv import load_dotenv

load_dotenv()

from app.llm.factory import LLMFactory

from app.schemas.resume import ResumeInfo

from app.prompts.manager import PromptManager


llm = LLMFactory.create()


resume = """
我叫张三，今年26岁。

3年Python开发经验。

熟悉FastAPI

Docker

Redis

MySQL
"""


messages = PromptManager.build_resume_messages(
    resume
)


result = llm.chat(

    messages,

    response_model=ResumeInfo,

)

print(result)

print(result.name)

print(result.skills)

print(result.experience)