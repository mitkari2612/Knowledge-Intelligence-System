# Knowledge Intelligence System

## Project Name
**Knowledge Intelligence System (KIS)**

## Aim
To develop an intelligent document management and query processing system that leverages artificial intelligence to help users extract insights from documents through natural language interactions.

## Objective
- Enable users to upload and store documents securely in cloud storage
- Provide AI-powered query processing to extract information from documents
- Implement semantic search using vector embeddings for intelligent document retrieval
- Create an intuitive web interface for seamless user interaction
- Build a scalable RESTful API for integration with other applications

## Problem Statement
Organizations and individuals face significant challenges in managing and extracting information from large volumes of documents:

1. **Information Overload**: Manual searching through documents is time-consuming and inefficient
2. **Knowledge Silos**: Important information remains trapped in documents without easy access
3. **Time-Consuming Queries**: Finding specific information requires reading entire documents
4. **Lack of Intelligence**: Traditional search only matches keywords, missing context and semantics
5. **Scalability Issues**: As document volumes grow, manual management becomes impossible

**Solution**: An AI-powered system that understands natural language queries and retrieves relevant information from documents using advanced LLM technology and semantic search.

## Tech Stack

### Backend Technologies
- **Python 3.11+** - Core programming language
- **Flask 3.1.3** - Lightweight web framework for REST API
- **Flask-CORS 6.0.5** - Cross-Origin Resource Sharing support
- **LangChain 0.1.20** - LLM orchestration and document processing framework
- **LangChain-Google-GenAI 0.0.9** - Google Gemini AI integration
- **Google Generative AI 0.3.2** - Official Google AI SDK
- **Pydantic 1.10.26** - Data validation and settings management

### AI/ML Technologies
- **Google Gemini AI** - Advanced large language model for natural language processing
  - Models used: gemini-2.0-flash, gemini-2.5-flash, gemini-flash-latest
  - Capabilities: Text generation, semantic understanding, question answering
- **LangChain** - Framework for building LLM-powered applications
- **Vector Embeddings** - For semantic search and document similarity

### Cloud & Storage
- **AWS S3 (Boto3 1.43.46)** - Cloud storage for document uploads
  - Secure document storage
  - Scalable file management
  - Access control and permissions

### Document Processing
- **PyPDF 6.14.2** - PDF text extraction and parsing
- **Tiktoken 0.13.0** - Token counting for LLM input management
- **Vector Database** - Semantic search and embeddings storage

### Frontend Technologies
- **HTML5** - Web page structure
- **CSS3** - Styling and responsive design
- **JavaScript (ES6+)** - Interactive functionality
- **Fetch API** - Asynchronous backend communication

### Development Tools
- **python-dotenv 1.2.2** - Environment variable management
- **Requests 2.34.2** - HTTP library for API calls
- **Werkzeug 3.1.8** - WSGI utility library

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Client Layer                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         Web Browser (HTML/CSS/JavaScript)            │  │
│  │  - Document Upload Interface                         │  │
│  │  - Query Input Interface                             │  │
│  │  - Response Display                                  │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ HTTP/HTTPS
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                      API Gateway Layer                       │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              Flask Web Server (Port 5000)            │  │
│  │  - CORS Enabled                                      │  │
│  │  - Request Routing                                   │  │
│  │  - Error Handling                                    │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│   Upload     │   │    Query     │   │    Health    │
│   Service    │   │   Service    │   │   Service    │
└──────────────┘   └──────────────┘   └──────────────┘
        │                   │                   │
        └───────────────────┼───────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│    LLM       │   │   Storage    │   │   Vector     │
│   Service    │   │   Service    │   │   Service    │
└──────────────┘   └──────────────┘   └──────────────┘
        │                   │                   │
        │                   │                   │
        ▼                   ▼                   ▼
┌─────────────────────────────────────────────────────────────┐
│                    External Services                         │
│  ┌────────────────┐  ┌────────────────┐  ┌──────────────┐ │
│  │ Google Gemini  │  │   AWS S3       │  │   Vector     │ │
│  │      AI        │  │   Storage      │  │   Database   │ │
│  │ - LLM Inference│  │ - File Storage │  │ - Embeddings │ │
│  │ - Text Gen     │  │ - Documents    │  │ - Semantic   │ │
│  │ - Q&A          │  │ - Access Ctrl  │  │   Search     │ │
│  └────────────────┘  └────────────────┘  └──────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## Architecture Components

### 1. Presentation Layer
- **Web Interface**: Single-page application with HTML/CSS/JavaScript
- **File Upload**: Drag-and-drop PDF upload functionality
- **Query Interface**: Text input for natural language questions
- **Response Display**: Formatted AI-generated responses

### 2. API Layer
- **Flask REST API**: Handles HTTP requests and responses
- **CORS Support**: Enables cross-origin requests for frontend
- **Request Validation**: Input validation and error handling
- **Response Formatting**: JSON responses for API consumers

### 3. Service Layer
- **LLM Service**: Manages Google Gemini AI interactions
  - Model initialization and fallback
  - Query processing and response generation
  - Error handling and retries
  
- **Storage Service**: Handles AWS S3 operations
  - File upload/download
  - Document management
  - Access control
  
- **Vector Service**: Manages document embeddings
  - Text chunking and embedding generation
  - Semantic search
  - Similarity matching

### 4. Data Layer
- **AWS S3**: Cloud storage for uploaded documents
- **Vector Database**: Stores document embeddings for semantic search
- **Environment Configuration**: Secure API key management

### 5. AI/ML Layer
- **Google Gemini AI**: Core LLM for natural language processing
  - Automatic model selection (tries multiple models)
  - Quota management and fallback
  - Response generation
  
- **LangChain**: LLM orchestration framework
  - Document processing chains
  - Prompt templates
  - Memory management

## Key Features

### 1. Document Upload
- **Supported Formats**: PDF documents
- **Upload Method**: Drag-and-drop or file selection
- **Storage**: Secure cloud storage on AWS S3
- **Validation**: File type and size validation
- **Feedback**: Real-time upload status

### 2. AI-Powered Query Processing
- **Natural Language Input**: Ask questions in plain English
- **Semantic Understanding**: AI understands context and meaning
- **Intelligent Responses**: Context-aware answers from documents
- **Multi-Model Support**: Automatic fallback between Gemini models
- **Error Handling**: Graceful handling of quota limits and errors

### 3. Smart Document Management
- **Vector Embeddings**: Documents converted to semantic vectors
- **Similarity Search**: Find relevant document sections
- **Context Retrieval**: Extract most relevant information
- **Scalable Storage**: Handle large document collections

### 4. RESTful API
- **Health Check**: `GET /api/health`
- **Query API**: `POST /api/query`
- **Upload API**: `POST /api/upload`
- **JSON Responses**: Standardized API responses
- **Error Handling**: Comprehensive error messages

### 5. User-Friendly Interface
- **Clean Design**: Modern, intuitive web interface
- **Responsive Layout**: Works on desktop and mobile
- **Real-time Feedback**: Loading indicators and status messages
- **Error Messages**: Clear, helpful error descriptions

## Data Flow

### Document Upload Flow
```
1. User selects PDF file
   ↓
2. Frontend sends POST request to /api/upload
   ↓
3. Flask backend receives file
   ↓
4. Storage Service uploads to AWS S3
   ↓
5. Document text extracted using PyPDF
   ↓
6. Text chunked into smaller segments
   ↓
7. Vector embeddings generated
   ↓
8. Embeddings stored in vector database
   ↓
9. Success response sent to user
```

### Query Processing Flow
```
1. User enters question in web interface
   ↓
2. Frontend sends POST request to /api/query
   ↓
3. Flask backend receives query
   ↓
4. Query converted to vector embedding
   ↓
5. Vector database searches for similar content
   ↓
6. Relevant document sections retrieved
   ↓
7. LLM Service processes query with context
   ↓
8. Google Gemini generates response
   ↓
9. Response formatted and sent to user
   ↓
10. Frontend displays answer
```

## Configuration

### Environment Variables
```env
# Google AI Configuration
GOOGLE_API_KEY = "your_google_ai_studio_api_key"

# AWS S3 Configuration
AWS_ACCESS_KEY = "your_aws_access_key"
AWS_SECRET_KEY = "your_aws_secret_key"
AWS_BUCKET_NAME = "your_bucket_name"
```

### Model Configuration
The system automatically tries multiple Gemini models in this order:
1. gemini-2.0-flash (stable, recommended)
2. gemini-2.0-flash-001
3. gemini-2.5-flash
4. gemini-2.5-pro
5. gemini-flash-latest
6. gemini-pro-latest
7. gemini-2.0-flash-lite
8. gemini-2.5-flash-lite

## Installation & Setup

### Prerequisites
- Python 3.11 or higher
- Google AI Studio account (for API key)
- AWS account (for S3 storage)
- Git (for cloning repository)

### Step 1: Clone Repository
```bash
git clone https://github.com/mitkari2612/Knowledge-Intelligence-System.git
cd Knowledge-Intelligence-System
```

### Step 2: Create Virtual Environment
```bash
# Using Conda (Recommended)
conda create -n llmapp python=3.11 -y
conda activate llmapp

# OR using venv
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment
1. Get Google AI API key from: https://makersuite.google.com/app/apikey
2. Enable Generative AI API: https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com
3. Enable billing: https://console.cloud.google.com/billing
4. Create AWS S3 bucket
5. Update `app/.env` with your credentials

### Step 5: Run Application
```bash
python run.py
```

### Step 6: Access Application
- Web Interface: http://localhost:5000
- API Health Check: http://localhost:5000/api/health

## API Documentation

### Base URL
```
http://localhost:5000
```

### Endpoints

#### 1. Health Check
```http
GET /api/health
```

**Response:**
```json
{
  "status": "healthy",
  "message": "Knowledge Intelligence System is running"
}
```

#### 2. Query API
```http
POST /api/query
Content-Type: application/json

{
  "query": "What is machine learning?"
}
```

**Response:**
```json
{
  "response": "Machine learning is a subset of artificial intelligence...",
  "status": "success"
}
```

#### 3. Upload API
```http
POST /api/upload
Content-Type: multipart/form-data

Form Data:
- file: [PDF file]
```

**Response:**
```json
{
  "message": "File uploaded successfully",
  "filename": "document.pdf",
  "status": "success"
}
```

## Usage Examples

### Web Interface Usage
1. **Upload Document:**
   - Click "Select Files" or drag and drop a PDF
   - Wait for upload confirmation
   - Document is processed and indexed

2. **Ask Questions:**
   - Type your question in the text area
   - Press Ctrl+Enter or click "Submit Query"
   - View AI-generated response

### API Usage Examples

#### Using cURL
```bash
# Health check
curl http://localhost:5000/api/health

# Query
curl -X POST http://localhost:5000/api/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What are the main topics in this document?"}'

# Upload
curl -X POST http://localhost:5000/api/upload \
  -F "file=@document.pdf"
```

#### Using Python
```python
import requests

# Query
response = requests.post(
    "http://localhost:5000/api/query",
    json={"query": "What is machine learning?"}
)
print(response.json())

# Upload
with open("document.pdf", "rb") as f:
    response = requests.post(
        "http://localhost:5000/api/upload",
        files={"file": f}
    )
print(response.json())
```

#### Using JavaScript
```javascript
// Query
const response = await fetch('http://localhost:5000/api/query', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({query: 'What is AI?'})
});
const data = await response.json();
console.log(data);

// Upload
const formData = new FormData();
formData.append('file', fileInput.files[0]);

const response = await fetch('http://localhost:5000/api/upload', {
  method: 'POST',
  body: formData
});
const data = await response.json();
console.log(data);
```

## Troubleshooting

### Issue: 404 Model Not Found
**Error**: `404 models/gemini-1.5-flash is not found`

**Solution**: 
- The system automatically tries multiple models
- Ensure you've enabled Generative AI API in Google Cloud Console
- Create a NEW API key after enabling the API
- Check available models: `python app/list_available_models.py`

### Issue: 429 Quota Exceeded
**Error**: `429 RESOURCE_EXHAUSTED: Quota exceeded`

**Solution**:
- Free tier limits: 15 requests/minute, 1,500 requests/day
- Wait for quota reset (1 minute or until midnight PST)
- Check usage: https://ai.dev/rate-limit
- Upgrade to paid plan: https://console.cloud.google.com/billing

### Issue: 503 Service Unavailable
**Error**: `503 UNAVAILABLE: High demand`

**Solution**:
- The model is temporarily overloaded
- The system automatically tries alternative models
- Wait a few minutes and try again

### Issue: Import Error (Pydantic)
**Error**: `ImportError: cannot import name 'model_serializer'`

**Solution**:
```bash
pip install -r requirements.txt --force-reinstall
```

### Issue: AWS Upload Failed
**Error**: `Error uploading file`

**Solution**:
- Verify AWS credentials in `app/.env`
- Check S3 bucket permissions
- Ensure bucket exists in specified region
- Verify IAM user has S3 write permissions

## Development

### Project Structure
```
Knowledge-Intelligence-System/
├── app/
│   ├── __init__.py              # Flask app initialization
│   ├── main.py                  # Main Flask application and routes
│   ├── config.py                # Configuration settings
│   ├── .env                     # Environment variables (not in git)
│   ├── check_models.py          # Script to test API key and models
│   ├── list_available_models.py # Script to list available models
│   ├── models/
│   │   ├── __init__.py
│   │   └── vector_stotre.py     # Vector database operations
│   ├── services/
│   │   ├── __init__.py
│   │   ├── llm_service.py       # Google Gemini AI integration
│   │   └── storage_service.py   # AWS S3 operations
│   ├── static/
│   │   └── style.css            # Frontend styling
│   └── templates/
│       └── index.html           # Web interface
├── requirements.txt             # Python dependencies
├── run.py                       # Application entry point
├── Dockerfile                   # Docker configuration
├── .gitignore                   # Git ignore file
├── LICENSE                      # MIT License
└── README.md                    # This file
```

### Running in Debug Mode
The application runs in debug mode by default. For production deployment:

```bash
# Using Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app.main:app

# Using uWSGI
uwsgi --http :5000 --module app.main:app --processes 4
```

### Docker Deployment
```bash
# Build image
docker build -t knowledge-intelligence-system .

# Run container
docker run -p 5000:5000 knowledge-intelligence-system
```

### Running Tests
```bash
# Check API key and models
python app/check_models.py

# List available models
python app/list_available_models.py
```

## Performance Considerations

### Free Tier Limits
- **Requests Per Minute (RPM)**: 15
- **Requests Per Day (RPD)**: 1,500
- **Tokens Per Minute**: 1,000,000
- **Concurrent Requests**: Limited

### Optimization Strategies
1. **Caching**: Cache frequent queries
2. **Rate Limiting**: Implement client-side rate limiting
3. **Batch Processing**: Process multiple documents efficiently
4. **Model Selection**: Use faster models for simple queries
5. **Token Management**: Optimize prompt length

## Security Considerations

1. **API Key Protection**:
   - Never commit `.env` to version control
   - Rotate API keys regularly
   - Use environment variables

2. **AWS Security**:
   - Use IAM roles with minimal permissions
   - Enable S3 bucket encryption
   - Use presigned URLs for secure access

3. **Input Validation**:
   - Validate file types and sizes
   - Sanitize user inputs
   - Implement rate limiting

4. **CORS Configuration**:
   - Restrict allowed origins in production
   - Use HTTPS in production

## Future Enhancements

1. **Multi-Document Support**: Query across multiple documents simultaneously
2. **Advanced Search**: Filter by date, author, document type
3. **User Authentication**: Multi-user support with authentication
4. **Document History**: Track query history and document access
5. **Export Features**: Export responses as PDF, DOCX
6. **Collaboration**: Share documents and queries with team members
7. **Analytics**: Usage statistics and insights
8. **Custom Models**: Fine-tuned models for specific domains
9. **Offline Mode**: Local LLM support for offline usage
10. **Mobile App**: Native mobile applications

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For issues and questions:
- Open an issue on GitHub: https://github.com/mitkari2612/Knowledge-Intelligence-System/issues
- Check the troubleshooting section in this README
- Review Google AI Studio documentation: https://ai.google.dev/docs
- Review LangChain documentation: https://python.langchain.com/

## Acknowledgments

- **Google AI Studio** - For providing the Gemini AI API
- **LangChain** - For the excellent LLM orchestration framework
- **AWS** - For reliable cloud storage services
- **Flask Community** - For the lightweight web framework
- **Open Source Community** - For various libraries and tools

## Contact

For queries and support:
- GitHub: https://github.com/mitkari2612/Knowledge-Intelligence-System
- Email: mitkari2612@gmail.com

---

**Version**: 1.0.0  
**Last Updated**: July 2026  
**Status**: Active Development