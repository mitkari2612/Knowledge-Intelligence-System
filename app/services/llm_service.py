from langchain_google_genai import ChatGoogleGenerativeAI
from ..config import Config


class LLMService:
    def __init__(self):
        try:
            self.llm = ChatGoogleGenerativeAI(
                temperature=0.7,
                model="gemini-pro-latest",
                google_api_key=Config.GOOGLE_API_KEY
            )
            print("LLM Service initialized successfully with Google Gemini")
        except Exception as e:
            print(f"Error initializing LLM: {e}")
            self.llm = None
    
    def get_response(self, query):
        try:
            if not self.llm:
                return "LLM Service not initialized. Check your Google API key."
            
            print(f"Processing query: {query}")
            response = self.llm.invoke(query)
            response_text = response.content if hasattr(response, 'content') else str(response)
            print(f"Response: {response_text}")
            return response_text
        except Exception as e:
            print(f"Error getting LLM response: {e}")
            import traceback
            traceback.print_exc()
            return f"Error: {str(e)}"
                
            
        