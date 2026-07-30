# 🎓 AIT Admission Assistant Chatbot

An AI-powered admission assistant chatbot that helps students get accurate information about admissions using official admission documents.

The chatbot uses **Retrieval Augmented Generation (RAG)** to retrieve relevant information from admission documents and generate context-based responses.

---

## 🚀 Features

- 🔐 Student Registration and Login
- 🤖 AI-powered admission query assistant
- 📄 PDF document-based question answering
- 🔍 Semantic search using embeddings
- 🧠 Retrieval Augmented Generation (RAG)
- 💬 Interactive React chatbot interface
- 🔒 JWT-based authentication
- 🗄️ Database integration for student management

---

## 🏗️ Project Architecture
admission_chatbot
│
├── backend
│ ├── FastAPI Backend
│ ├── Authentication (JWT)
│ ├── PostgreSQL Database
│ ├── LangChain RAG Pipeline
│ ├── Chroma Vector Database
│ └── Ollama LLM Integration
│
├── frontend
│ ├── React + Vite
│ ├── Chat Interface
│ ├── Authentication Pages
│ └── API Integration
│
└── documents
└── Admission PDF Knowledge Base


---

## 🛠️ Tech Stack

### Frontend
- React.js
- Vite
- Axios
- CSS

### Backend
- FastAPI
- Python
- SQLAlchemy
- PostgreSQL
- JWT Authentication

### AI / ML
- LangChain
- Ollama
- Llama 3.2
- ChromaDB
- HuggingFace Embeddings

---

## 🔄 How It Works

1. Admission documents are loaded and split into smaller chunks.
2. Text chunks are converted into vector embeddings.
3. Embeddings are stored in ChromaDB.
4. User questions are converted into embeddings.
5. Relevant document sections are retrieved.
6. LLM generates an answer using only retrieved context.

---

## 📂 Backend Setup

```bash
cd backend

python -m venv venv

# Activate environment

# Windows
venv\Scripts\activate

pip install -r requirements.txt
Create a .env file:

DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key

Run backend:

uvicorn app.main:app --reload
📂 Frontend Setup
cd frontend

npm install

npm run dev

Frontend runs on:

http://localhost:5173
🎯 Future Improvements
Voice-based admission assistant
Deployment using Docker and AWS
Admin dashboard
More document sources
Conversation history
👩‍💻 Author

Garima Bhardwaj

BE Electronics & Telecommunication Engineering
Army Institute of Technology, Pune