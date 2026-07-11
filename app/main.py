from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from .config import Config
from .services.llm_service import LLMService
from .services.storage_service import StorageService
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_object(Config)
CORS(app)

# Initialize services
llm_service = LLMService()
storage_service = StorageService()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/query', methods=['POST'])
def query():
    try:
        data = request.json
        query_text = data.get('query', '')
        
        if not query_text:
            return jsonify({'error': 'Query cannot be empty'}), 400
        
        response = llm_service.get_response(query_text)
        return jsonify({'response': response})
    except Exception as e:
        print(f"Error in query endpoint: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/upload', methods=['POST'])
def upload():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        success = storage_service.upload_file(file, file.filename)
        if success:
            return jsonify({'message': 'File uploaded successfully'})
        else:
            return jsonify({'error': 'Failed to upload file'}), 500
    except Exception as e:
        print(f"Error in upload endpoint: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
