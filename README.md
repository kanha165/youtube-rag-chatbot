# 🎥 YouTube RAG Chatbot

An AI-powered YouTube Question Answering System built using Retrieval-Augmented Generation (RAG), FastAPI, Streamlit, ChromaDB, MySQL, and Groq LLM.

This application allows users to process YouTube videos, extract transcripts, store semantic embeddings, and ask questions about video content using Large Language Models.

---

# 🚀 Features

### 📺 YouTube Video Processing

* Extract YouTube Video ID
* Fetch Video Transcripts
* Multi-language Transcript Support
* Automatic Transcript Cleaning
* Intelligent Text Chunking

### 🧠 RAG Pipeline

* Semantic Search
* Context Retrieval
* Vector Database Integration
* Relevant Chunk Selection
* Grounded Response Generation

### 🤖 AI Question Answering

* Groq LLM Integration
* Context-Aware Responses
* Hallucination Reduction
* Fast Inference

### 💾 Data Persistence

* MySQL Database
* Session Management
* Video History Storage
* Chat History Storage

### 🎨 User Interface

* Streamlit Frontend
* Sidebar Video Management
* Chat Interface
* Session-Based User Experience

---

# 🏗️ System Architecture

```text
User
 │
 ▼
Streamlit Frontend
 │
 ▼
FastAPI Backend
 │
 ├── YouTube Transcript API
 │
 ├── ChromaDB Vector Store
 │
 ├── MySQL Database
 │
 └── Groq LLM
 │
 ▼
AI Generated Answer
```

---

# ⚙️ Tech Stack

## Backend

* FastAPI
* Python
* SQLAlchemy
* Uvicorn

## Frontend

* Streamlit

## Database

* MySQL

## Vector Database

* ChromaDB

## LLM

* Groq

## AI Components

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Context Retrieval
* Prompt Engineering

---

# 📁 Project Structure

```text
youtube-rag-chatbot/

├── app/
│
├── routes/
│   ├── video.py
│   ├── chat.py
│   └── session.py
│
├── services/
│   ├── youtube_service.py
│   ├── vector_service.py
│   └── rag_service.py
│
├── database/
│   ├── db.py
│   └── models.py
│
├── models/
│   └── schemas.py
│
├── streamlit_app.py
│
├── requirements.txt
│
├── .env
│
└── README.md
```

---

# 🔄 RAG Workflow

## Step 1

User submits a YouTube URL.

## Step 2

System extracts the transcript.

## Step 3

Transcript is cleaned and chunked.

## Step 4

Chunks are stored in ChromaDB.

## Step 5

User asks a question.

## Step 6

Relevant chunks are retrieved.

## Step 7

Context is sent to Groq LLM.

## Step 8

AI-generated answer is returned.

---

# 🗄️ Database Schema

## Sessions Table

```sql
CREATE TABLE sessions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    session_id VARCHAR(255) UNIQUE
);
```

## Videos Table

```sql
CREATE TABLE videos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    session_id VARCHAR(255),
    video_id VARCHAR(255),
    video_url TEXT
);
```

## Chats Table

```sql
CREATE TABLE chats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    session_id VARCHAR(255),
    video_id VARCHAR(255),
    question TEXT,
    answer LONGTEXT
);
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=your_groq_api_key

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=password
MYSQL_DATABASE=youtube_rag
```

---

# 📦 Installation

## Clone Repository

```bash
git clone https://github.com/kanha165/youtube-rag-chatbot.git

cd youtube-rag-chatbot
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Backend

```bash
uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Frontend

```bash
streamlit run streamlit_app.py
```

Frontend:

```text
http://localhost:8501
```

---

# 🔌 API Endpoints

## Session APIs

### Create Session

```http
POST /session
```

### Get Session

```http
GET /session/{session_id}
```

---

## Video APIs

### Process Video

```http
POST /process-video
```

### Get Videos

```http
GET /videos/{session_id}
```

### Get Video Details

```http
GET /video/{session_id}/{video_id}
```

### Delete Video

```http
DELETE /video/{session_id}/{video_id}
```

---

## Chat APIs

### Ask Question

```http
POST /ask
```

### Chat History

```http
GET /chat-history/{session_id}/{video_id}
```

### Delete Chat

```http
DELETE /chat/{chat_id}
```

---

## Analytics APIs

### Statistics

```http
GET /stats
```

---

# 🌟 Example Usage

## Process Video

```json
{
  "session_id": "abc123",
  "url": "https://www.youtube.com/watch?v=xxxxxx"
}
```

## Ask Question

```json
{
  "session_id": "abc123",
  "video_id": "xxxxxx",
  "question": "What is this video about?"
}
```

---

# 📈 Future Improvements

* User Authentication
* JWT Security
* Pinecone Integration
* Qdrant Cloud Support
* Multi-Video RAG
* Streaming Responses
* LangChain Integration
* LangGraph Agents
* Redis Cache
* Docker Deployment
* Kubernetes Deployment
* CI/CD Pipeline
* Admin Dashboard

---

# 🧪 Testing

```bash
pytest
```

---

# 🚀 Deployment

## Backend

Render

## Frontend

Streamlit Cloud

## Database

Railway MySQL

## Vector Database

ChromaDB / Pinecone / Qdrant

---

# 👨‍💻 Author

**Kanha Patidar**

B.Tech CSIT
AI Engineer | Python Developer | Generative AI Enthusiast

GitHub:

https://github.com/kanha165

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project useful:

* Star the repository
* Fork the project
* Share with others

Happy Coding 🚀
