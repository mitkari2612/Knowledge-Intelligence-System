from langchain_google_genai import ChatGoogleGenerativeAI
from ..config import Config


class LLMService:
    def __init__(self):
        # Try multiple model names in order of preference
        # Based on available models from your API key
        model_names = [
            "gemini-2.0-flash",         # Stable 2.0 flash (recommended)
            "gemini-2.0-flash-001",     # Stable 2.0 flash version
            "gemini-2.5-flash",         # Latest 2.5 flash
            "gemini-2.5-pro",           # Latest 2.5 pro
            "gemini-flash-latest",      # Flash latest
            "gemini-pro-latest",        # Pro latest
            "gemini-2.0-flash-lite",    # 2.0 flash lite
            "gemini-2.5-flash-lite"     # 2.5 flash lite
        ]
        
        self.llm = None
        for model_name in model_names:
            try:
                print(f"Trying to initialize with model: {model_name}")
                self.llm = ChatGoogleGenerativeAI(
                    temperature=0.7,
                    model=model_name,
                    google_api_key=Config.GOOGLE_API_KEY
                )
                print(f"✓ LLM Service initialized successfully with Google Gemini ({model_name})")
                break
            except Exception as e:
                error_msg = str(e)
                if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
                    print(f"✗ {model_name} has exceeded quota, trying next model...")
                elif "503" in error_msg or "UNAVAILABLE" in error_msg:
                    print(f"✗ {model_name} is temporarily unavailable (high demand), trying next...")
                else:
                    print(f"✗ Failed to initialize {model_name}: {error_msg[:100]}")
                continue
        
        if not self.llm:
            print("\n" + "=" * 70)
            print("ERROR: Could not initialize any Gemini model")
            print("=" * 70)
            print("\nAll models have exceeded their quota or are unavailable.")
            print("\nSolutions:")
            print("1. Wait for quota to reset:")
            print("   - Per minute limit: Wait 1-2 minutes")
            print("   - Per day limit: Wait until tomorrow (resets at midnight PST)")
            print("\n2. Check your quota usage:")
            print("   - Visit: https://ai.dev/rate-limit")
            print("\n3. Upgrade to paid plan:")
            print("   - Visit: https://console.cloud.google.com/billing")
            print("\n4. Free tier limits:")
            print("   - 15 requests per minute")
            print("   - 1,500 requests per day")
            print("=" * 70)
    
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
                
            
        