from pydantic import BaseModel

class ResumeExtractRequest(BaseModel):
    """
    简历提取请求
    """
    text: str 