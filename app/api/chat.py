from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.services.chat_service import ChatService
from app.services.extract_service import ExtractService


router = APIRouter()

service = ChatService()

@router.post("")
async def chat(
    data: dict
):
    question = data.get("question")

    answer = await service.chat(
        question=question
    )

    return {"result": answer}

@router.post("/stream")
async def stream_chat(
    data: dict
):
    question = data.get("question")

    generator = await service.stream(
        question=question
    )

    return StreamingResponse(
        generator,
        media_type="text/plain"
    )

