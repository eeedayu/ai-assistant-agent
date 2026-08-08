from pydantic import BaseModel, Field


class ResumeInfo(BaseModel):
    """
    简历结构化信息
    """

    name: str = Field(
        description="候选人的姓名"
    )

    age: int = Field(
        description="候选人的年龄"
    )

    experience: int | None = Field(default=None,
        description="工作年限"
    )

    skills: list[str] = Field(
        default_factory=list,
        description="候选人掌握的技能列表"
    )