from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title="YouTube RAG API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "YouTube RAG Running"
    }
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)    

from app.routes.video import router

app.include_router(router)

from app.routes.chat import router as chat_router

app.include_router(chat_router)



from app.routes.session import router as session_router

app.include_router(
    session_router
)