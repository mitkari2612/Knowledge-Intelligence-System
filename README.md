# 🧠 Knowledge Intelligence System

An AI-powered **Retrieval-Augmented Generation (RAG)** application that enables users to upload documents, search through them using semantic similarity, and interact with their knowledge base through a conversational interface. The system retrieves relevant information from uploaded documents and generates accurate, context-aware answers using a Large Language Model (LLM), complete with source citations.

---

## 🚀 Features

- 📄 Upload and manage documents (PDF, TXT, Markdown)
- ✂️ Automatic document parsing and intelligent text chunking
- 🔍 Semantic search using vector embeddings
- 🤖 AI-powered question answering using Retrieval-Augmented Generation (RAG)
- 📚 Source citations with document references
- 💬 Persistent chat interface for conversations
- 🗂️ Collection/Workspace management
- ⚙️ Configurable chunk size and retrieval parameters
- 📊 Admin dashboard for document management and analytics
- 📝 Query history and logging
- 🔄 Document re-indexing and deletion

---

# 🏗️ System Architecture

```
                        +----------------------+
                        |      Frontend        |
                        |      (React)         |
                        +----------+-----------+
                                   |
                                   |
                            REST API Requests
                                   |
                                   ▼
                      +-------------------------+
                      |   FastAPI Backend       |
                      |  (API & Orchestration)  |
                      +-----------+-------------+
                                  |
             +--------------------+---------------------+
             |                                          |
             ▼                                          ▼
   Document Upload                             User Question
             |                                          |
             ▼                                          ▼
     Document Parsing                         Query Embedding
             |                                          |
             ▼                                          ▼
      Text Chunking                           Vector Similarity Search
             |                                          |
             ▼                                          ▼
      Embedding Model                      Retrieve Top-K Chunks
             |                                          |
             +--------------------+---------------------+
                                  |
                                  ▼
                          Prompt Construction
                                  |
                                  ▼
                            Large Language Model
                                  |
                                  ▼
                      Answer + Source Citations
                                  |
                                  ▼
                              Frontend UI
```

---

# 📌 Project Workflow

## 1️⃣ Document Upload

Users upload documents through the web interface.

Supported formats:

- PDF
- TXT
- Markdown

The backend stores the uploaded file securely.

---

## 2️⃣ Document Parsing

The uploaded document is converted into plain text.

Example:

```
Employee Handbook.pdf

↓

Extract Text

↓

Employees receive 20 casual leaves...
```

---

## 3️⃣ Text Chunking

Large documents are divided into smaller chunks.

Example:

```
Chunk 1
Introduction

Chunk 2
Leave Policy

Chunk 3
Salary Policy

Chunk 4
Working Hours
```

Chunking improves retrieval accuracy while staying within the LLM context window.

---

## 4️⃣ Embedding Generation

Each chunk is converted into a high-dimensional numerical vector using an embedding model.

```
Text

↓

Embedding Model

↓

[0.25, 0.61, 0.82, ...]
```

Embeddings capture the semantic meaning of the text.

---

## 5️⃣ Vector Storage

Each chunk is stored inside the vector database along with metadata.

Stored information:

- Chunk Text
- Embedding Vector
- Document Name
- Chunk ID
- Page Number
- Upload Date
- Tags

---

## 6️⃣ User Query

The user asks a natural language question.

Example:

```
How many casual leaves are provided?
```

---

## 7️⃣ Query Embedding

The question is converted into an embedding vector.

```
Question

↓

Embedding

↓

Vector
```

---

## 8️⃣ Semantic Retrieval

The vector database compares the query vector against all stored document vectors.

Using similarity search, it retrieves the most relevant chunks.

```
Question Vector

↓

Similarity Search

↓

Top-K Relevant Chunks
```

---

## 9️⃣ Prompt Construction

The backend combines:

- System Instructions
- Retrieved Context
- User Question

into a single prompt.

```
System Prompt

+

Retrieved Chunks

+

User Question

↓

LLM
```

---

## 🔟 AI Answer Generation

The Large Language Model generates a response using only the retrieved document context.

Example:

```
Employees receive 20 casual leaves annually.

Source:
Employee Handbook
Page 12
```

---

## 1️⃣1️⃣ Response Display

The frontend displays:

- AI-generated answer
- Source documents
- Citation references
- Chat history

---

# 🧠 Retrieval-Augmented Generation (RAG)

This project uses the RAG architecture.

```
Documents

↓

Chunking

↓

Embeddings

↓

Vector Database

↓

User Question

↓

Embedding

↓

Similarity Search

↓

Relevant Chunks

↓

Prompt

↓

LLM

↓

Answer with Citations
```

Unlike a standard chatbot, the model answers only from uploaded documents, reducing hallucinations and improving reliability.

---

# 💻 Tech Stack

## Frontend

- React.js
- Tailwind CSS
- Axios

---

## Backend

- FastAPI
- Python

---

## AI & Machine Learning

- OpenAI API
- LangChain
- Embedding Model

---

## Database

- PostgreSQL / SQLite
- ChromaDB / pgvector (Vector Database)

---

## File Processing

- PyPDF
- Markdown Parser
- Text Processing Utilities

---

## Deployment & DevOps

- Docker
- Environment Variables (.env)
- Git & GitHub

---

# 📂 Project Structure

```
Knowledge-Intelligence-System/

│── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   ├── hooks/
│   └── services/
│
│── backend/
│   ├── api/
│   ├── services/
│   ├── models/
│   ├── routes/
│   ├── embeddings/
│   ├── rag/
│   ├── vectorstore/
│   └── utils/
│
│── storage/
│
│── database/
│
│── docs/
│
│── requirements.txt
│── package.json
│── docker-compose.yml
│── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/knowledge-intelligence-system.git

cd knowledge-intelligence-system
```

---

## Backend

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn main:app --reload
```

---

## Frontend

```bash
cd frontend
```

Install packages

```bash
npm install
```

Start application

```bash
npm run dev
```

---

# 🔐 Environment Variables

Create a `.env` file.

```
OPENAI_API_KEY=your_openai_api_key

DATABASE_URL=your_database_url

VECTOR_DB_PATH=./vectorstore

MODEL_NAME=gpt-4.1

EMBEDDING_MODEL=text-embedding-3-small
```

---

# 📊 Core Functionalities

- Document Upload
- Document Parsing
- Text Chunking
- Embedding Generation
- Vector Database Storage
- Semantic Search
- Retrieval-Augmented Generation
- Conversational Chat
- Source Citations
- Collection Management
- Admin Dashboard
- Query Logging
- Analytics

---

# 🎯 Future Enhancements

- Multi-user authentication
- Role-Based Access Control (RBAC)
- Multi-tenant architecture
- OCR for scanned PDFs
- Web page ingestion
- Audio and video transcription
- Hybrid Search (Keyword + Vector Search)
- Streaming AI responses
- Feedback-based ranking
- Local LLM support
- Kubernetes deployment
- Cloud storage integration
- Document versioning

---

# 📈 Performance Goals

- Answer generation in under **5–7 seconds**
- Support for hundreds of thousands of document chunks
- Reliable document ingestion
- Configurable retrieval parameters
- Scalable architecture

---

# 🎓 Learning Outcomes

This project demonstrates practical implementation of:

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Vector Databases
- Semantic Search
- Embeddings
- Prompt Engineering
- FastAPI
- React
- REST APIs
- AI-powered Knowledge Management Systems
- End-to-End Full Stack AI Development

---

# 🤝 Contributing

Contributions, feature requests, and suggestions are welcome.

Feel free to fork the repository and submit a pull request.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Ajay Mitkari**

- 🎓 B.Tech – Electronics & Telecommunication Engineering
- 🎓 PG-Diploma in Big Data Analytics (CDAC)
- 💡 AI | Machine Learning | Generative AI | Data Engineering

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!





















# Knowledge-Intelligence-System


 How to run?

### STEPS:


### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n llmapp python=3.11 -y
```

```bash
conda activate llmapp
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app/main.py
```
