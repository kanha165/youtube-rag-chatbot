from fastapi import APIRouter
from app.models.schemas import ChatRequest

from app.services.vector_service import (
    get_context
)

from app.services.rag_service import (
    generate_answer
)

from app.database.db import SessionLocal
from app.database.models import Chat

router = APIRouter(
    tags=["Chat"]
)


@router.post("/ask")
def ask_question(data: ChatRequest):

    # Get Context
    context = get_context(
    data.question,
    data.video_id
        )

    print("\n========== CONTEXT ==========")
    print(context)
    print("========== END ==========\n")

    # Generate Answer
    answer = generate_answer(
        data.question,
        context
    )

    # Save Chat In MySQL
    db = SessionLocal()

    try:

        chat = Chat(
            session_id=data.session_id,
            video_id=data.video_id,
            question=data.question,
            answer=answer
        )

        db.add(chat)
        db.commit()

    finally:
        db.close()

    return {
        "question": data.question,
        "answer": answer
    }


@router.get("/chat-history/{session_id}/{video_id}")
def chat_history(
    session_id: str,
    video_id: str
):

    db = SessionLocal()

    try:

        chats = db.query(Chat).filter(
            Chat.session_id == session_id,
            Chat.video_id == video_id
        ).all()

        return [
            {
                "question": c.question,
                "answer": c.answer
            }
            for c in chats
        ]

    finally:
        db.close()
        
@router.delete("/chat/{chat_id}")
def delete_chat(chat_id: int):

    db = SessionLocal()

    try:

        db.query(Chat).filter(
            Chat.id == chat_id
        ).delete()

        db.commit()

        return {
            "status": "deleted"
        }

    finally:
        db.close()
        
        
from app.database.models import (
    Session,
    Video,
    Chat
)


        
        
@router.get("/stats")
def stats():

    db = SessionLocal()

    try:

        return {

            "total_sessions":
            db.query(Session).count(),

            "total_videos":
            db.query(Video).count(),

            "total_chats":
            db.query(Chat).count()
        }

    finally:
        db.close()
  