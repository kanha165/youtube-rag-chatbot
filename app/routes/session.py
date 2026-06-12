from fastapi import APIRouter
from uuid import uuid4

from app.database.db import SessionLocal
from app.database.models import Session

router = APIRouter(
    tags=["Session"]
)


@router.post("/session")
def create_session():

    db = SessionLocal()

    try:

        session_id = str(
            uuid4()
        )

        new_session = Session(
            session_id=session_id
        )

        db.add(
            new_session
        )

        db.commit()

        return {
            "session_id": session_id
        }

    finally:

        db.close()
        
@router.get(
    "/session/{session_id}"
)
def get_session(session_id: str):

    db = SessionLocal()

    try:

        videos = db.query(Video).filter(
            Video.session_id == session_id
        ).count()

        chats = db.query(Chat).filter(
            Chat.session_id == session_id
        ).count()

        return {
            "session_id": session_id,
            "videos": videos,
            "chats": chats
        }

    finally:
        db.close()        