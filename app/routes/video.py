from fastapi import APIRouter

from app.models.schemas import VideoRequest

from app.database.db import SessionLocal
from app.database.models import Video

from app.services.youtube_service import (
    extract_video_id,
    get_transcript,
    transcript_to_text,
    chunk_text
)

from app.services.vector_service import (
    store_chunks,
    video_exists,
    collection
)


router = APIRouter(
    tags=["Videos"]
)

@router.post("/process-video")
def process_video(data: VideoRequest):

    # Extract Video ID
    video_id = extract_video_id(
        data.url
    )

    if not video_id:

        return {
            "status": "error",
            "message": "Invalid YouTube URL"
        }

    try:

        # If already in ChromaDB
        if video_exists(video_id):

            db = SessionLocal()

            try:

                video = Video(
                    session_id=data.session_id,
                    video_id=video_id,
                    video_url=data.url
                )

                db.add(video)
                db.commit()

            finally:

                db.close()

            return {
                "status": "already_processed",
                "video_id": video_id,
                "message": "Video already exists in ChromaDB"
            }

        # Get Transcript
        transcript = get_transcript(
            video_id
        )

        # Convert To Text
        text = transcript_to_text(
            transcript
        )

        # Create Chunks
        chunks = chunk_text(
            text
        )

        # Store In ChromaDB
        store_chunks(
            video_id,
            chunks
        )

        # Save In MySQL
        db = SessionLocal()

        try:

            video = Video(
                session_id=data.session_id,
                video_id=video_id,
                video_url=data.url
            )

            db.add(video)
            db.commit()

        finally:

            db.close()

        return {
            "status": "success",
            "video_id": video_id,
            "transcript_length": len(text),
            "total_chunks": len(chunks),
            "preview": text[:500]
        }

    except Exception as e:

        return {
            "status": "error",
            "video_id": video_id,
            "message": str(e)
        }


@router.get("/count")
def count_documents():

    return {
        "documents": collection.count()
    }
    
    
    

@router.get("/videos/{session_id}")
def get_videos(session_id: str):

    db = SessionLocal()

    try:

        videos = (
            db.query(Video)
            .filter(
                Video.session_id == session_id
            )
            .all()
        )

        return [
            {
                "video_id": v.video_id,
                "video_url": v.video_url
            }
            for v in videos
        ]

    finally:
        db.close()
        
        
@router.delete(
    "/video/{session_id}/{video_id}"
)
def delete_video(
    session_id: str,
    video_id: str
):

    db = SessionLocal()

    try:

        db.query(Video).filter(
            Video.session_id == session_id,
            Video.video_id == video_id
        ).delete()

        db.commit()

        return {
            "status": "deleted"
        }

    finally:
        db.close()     
        
        
      
@router.get(
    "/video/{session_id}/{video_id}"
)
def get_video_details(
    session_id: str,
    video_id: str
):

    db = SessionLocal()

    try:

        video = db.query(Video).filter(
            Video.session_id == session_id,
            Video.video_id == video_id
        ).first()

        if not video:
            return {
                "status": "not_found"
            }

        return {
            "video_id": video.video_id,
            "video_url": video.video_url
        }

    finally:
        db.close()                                               