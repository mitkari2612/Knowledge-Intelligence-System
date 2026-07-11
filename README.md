# Knowledge Intelligence System

An AI-powered web application for intelligent document management and query processing using Google's Gemini AI. Upload documents, store them in AWS S3, and get AI-powered responses to your queries.

## Features

- **Document Upload**: Upload PDF and other documents to AWS S3 storage
- **AI-Powered Queries**: Ask questions and get intelligent responses using Google Gemini AI
- **Vector Database**: Store and retrieve document embeddings for semantic search
- **RESTful API**: Easy-to-use API endpoints for integration
- **Web Interface**: User-friendly web UI for document management and querying
- **CORS Enabled**: Ready for frontend integration

## Tech Stack

### Backend
- **Flask** - Web framework
- **LangChain** - LLM orchestration framework
- **Google Generative AI** - Gemini AI models (gemini-pro-latest)
- **AWS S3** - Document storage
- **Vector Database** - Semantic search and embeddings
- **PyPDF** - PDF text extraction
- **Tiktoken** - Token counting for LLM

### Frontend
- **HTML/CSS/JavaScript** - Web interface
- **Fetch API** - Backend communication

## Prerequisites

- Python 3.11 or higher
- Google AI Studio API key
- AWS account with S3 bucket
- Conda (optional, for environment management)

## Installation

### Option 1: Using Conda (Recommended)

```bash
# Create conda environment
conda create -n llmapp python=3.11 -y

# Activate environment
conda activate llmapp
```

### Option 2: Using Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

### 1. Google AI Studio API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Update `app/.env` file:

```env
GOOGLE_API_KEY = "your_google_ai_studio_api_key"
```

### 2. AWS S3 Configuration

Update `app/.env` with your AWS credentials:

```env
AWS_ACCESS_KEY = "your_aws_access_key"
AWS_SECRET_KEY = "your_aws_secret_key"
AWS_BUCKET_NAME = "your_bucket_name"
```

## Running the Application

```bash
python run.py
```

The application will start at `http://0.0.0.0:5000`

Access the web interface at: `http://localhost:5000`

## Project Structure

```
Knowledge-Intelligence-System/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Flask application and routes
│   ├── config.py               # Configuration settings
│   ├── .env                    # Environment variables
│   ├── models/
│   │   ├── __init__.py
│   │   └── vector_stotre.py    # Vector database operations
│   ├── services/
│   │   ├── __init__.py
│   │   ├── llm_service.py      # Google Gemini AI integration
│   │   └── storage_service.py  # AWS S3 operations
│   ├── static/
│   │   └── style.css           # Frontend styling
│   └── templates/
│       └── index.html          # Web interface
├── requirements.txt            # Python dependencies
├── run.py                      # Application entry point
├── Dockerfile                  # Docker configuration
└── README.md                   # This file
```

## API Endpoints

### Health Check
```
GET /api/health
```
Returns application status.

### Query Endpoint
```
POST /api/query
Content-Type: application/json

{
    "query": "Your question here"
}
```
Returns AI-generated response.

### Upload Endpoint
```
POST /api/upload
Content-Type: multipart/form-data

Form Data:
- file: [your file]
```
Uploads document to AWS S3.

## Usage

### Web Interface

1. **Upload Documents**: 
   - Click "Select Files" or drag and drop files
   - Documents are uploaded to AWS S3

2. **Ask Questions**:
   - Type your question in the text area
   - Click "Submit Query" or press Ctrl+Enter
   - Get AI-powered responses

### API Usage

#### Example: Query API

```bash
curl -X POST http://localhost:5000/api/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is machine learning?"}'
```

#### Example: Upload API

```bash
curl -X POST http://localhost:5000/api/upload \
  -F "file=@document.pdf"
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Google AI Studio API key | Yes |
| `AWS_ACCESS_KEY` | AWS access key ID | Yes |
| `AWS_SECRET_KEY` | AWS secret access key | Yes |
| `AWS_BUCKET_NAME` | S3 bucket name | Yes |

## Dependencies

```
flask>=2.3.3
flask-cors>=4.0.0
werkzeug>=2.3.7
langchain>=0.1.0
langchain-google-genai>=0.0.5
google-generativeai>=0.3.0
python-dotenv>=0.19.0
boto3>=1.28.0
pypdf>=3.9.0
tiktoken>=0.5.1
requests>=2.31.0
```

## Troubleshooting

### Quota Exceeded Error

**Error**: `RESOURCE_EXHAUSTED: Quota exceeded`

**Solution**: 
- Check your quota at https://ai.dev/rate-limit
- Upgrade to paid plan at https://console.cloud.google.com/billing
- Wait for quota reset (usually daily/monthly)

### Model Not Found Error

**Error**: `404 NOT_FOUND: models/gemini-pro is not found`

**Solution**: The application uses `gemini-pro-latest` which is automatically mapped to the latest available model.

### CORS Errors

**Error**: `Failed to fetch`

**Solution**: Ensure `flask-cors` is installed and CORS is enabled in `app/main.py`.

### AWS Connection Errors

**Error**: `Error uploading file`

**Solution**: 
- Verify AWS credentials in `.env`
- Check S3 bucket permissions
- Ensure bucket exists in the specified region

## Development

### Running in Debug Mode

The application runs in debug mode by default. For production, use a WSGI server like Gunicorn:

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app.main:app
```

### Docker Deployment

```bash
# Build image
docker build -t knowledge-intelligence-system .

# Run container
docker run -p 5000:5000 knowledge-intelligence-system
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For issues and questions:
- Open an issue on GitHub
- Check the troubleshooting section
- Review Google AI Studio documentation: https://ai.google.dev/docs

## Acknowledgments

- Google AI Studio for Gemini AI API
- LangChain for LLM orchestration
- AWS for cloud storage
- Flask community for the web framework