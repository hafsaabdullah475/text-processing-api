from fastapi import APIRouter, HTTPException, status
from app.schemas import TextRequest, TextResponse
from app.services import process_text

router = APIRouter()

@router.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "ok"}
