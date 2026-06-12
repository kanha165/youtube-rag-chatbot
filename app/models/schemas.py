from pydantic import BaseModel

class VideoRequest(BaseModel):

    session_id: str
    url: str


class ChatRequest(BaseModel):

    session_id: str
    video_id: str
    question: str
    
class VideoRequest(BaseModel):

    session_id: str
    url: str