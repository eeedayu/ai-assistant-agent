from fastapi import APIRouter
from fastapi import HTTPException


from app.llm.factory import LLMFactory
from app.schemas.extract import ResumeExtractRequest
from app.schemas.resume import ResumeInfo
from app.services.extract_service import ExtractService 

router = APIRouter(prefix="/extract", tags=["Extract"])


@router.post("/resume", response_model=ResumeInfo)
async def extract_resume(
    request: ResumeExtractRequest
):
    try:
        llm = LLMFactory.create()
        service = ExtractService(llm)

        result = service.extract_resume(
            text=request.text
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
