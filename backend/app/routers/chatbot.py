from fastapi import APIRouter

from app.schemas import ChatRequest, ChatResponse
from app.chatbot.service import get_chat_response

router = APIRouter(
    prefix="/chat",
    tags=["Admission Chatbot"]
)


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = get_chat_response(request.question)

    return ChatResponse(answer=answer)