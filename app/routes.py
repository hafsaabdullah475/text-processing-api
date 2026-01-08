from fastapi import APIRouter, HTTPException, status
from app.schemas import TextRequest, TextResponse
from app.services import process_text

router = APIRouter()

@router.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "ok"}

@router.post(
    "/process-text",
    response_model=TextResponse,
    status_code=status.HTTP_200_OK
)
def process_text_endpoint(request: TextRequest):

    if not request.text.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Text is required"
        )

    result = process_text(request.text)
    return result
