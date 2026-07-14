import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("ERROR: GOOGLE_API_KEY not found in .env file")
    print("Please add your API key to app/.env file")
    exit(1)

print(f"Testing API key: {api_key[:15]}...")
print("-" * 50)

# Try to initialize the LLM with a simple model name
try:
    print("\nAttempting to connect to Google Gemini API...")
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=api_key,
        temperature=0.7
    )
    
    print("✓ API Key is valid!")
    print("\nTrying to get a response...")
    response = llm.invoke("Say hello")
    print(f"✓ Response received: {response.content}")
    print("\n" + "-" * 50)
    print("SUCCESS: Your API key is working with gemini-pro model")
    
except Exception as e:
    error_msg = str(e)
    print(f"✗ FAILED with error:")
    print(f"  {error_msg}")
    
    if "404" in error_msg:
        print("\n" + "=" * 50)
        print("DIAGNOSIS: Model not found (404 error)")
        print("=" * 50)
        print("\nPossible solutions:")
        print("1. Your API key may not have access to Gemini models")
        print("2. You need to enable the Generative AI API in Google Cloud Console")
        print("3. Visit: https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com")
        print("4. Make sure to create a NEW API key after enabling the API")
        
    elif "429" in error_msg or "quota" in error_msg.lower():
        print("\n" + "=" * 50)
        print("DIAGNOSIS: Quota exceeded")
        print("=" * 50)
        print("\nSolutions:")
        print("1. Wait for quota to reset (usually 1 minute for RPM, 1 day for RPD)")
        print("2. Check quota at: https://ai.dev/rate-limit")
        
    elif "API_KEY_INVALID" in error_msg or "invalid" in error_msg.lower():
        print("\n" + "=" * 50)
        print("DIAGNOSIS: Invalid API key")
        print("=" * 50)
        print("\nSolutions:")
        print("1. Get a new API key from: https://makersuite.google.com/app/apikey")
        print("2. Update the GOOGLE_API_KEY in app/.env file")
        
    else:
        print("\n" + "=" * 50)
        print("DIAGNOSIS: Unknown error")
        print("=" * 50)
        print("\nPlease check:")
        print("1. Your API key is correct")
        print("2. Generative AI API is enabled in Google Cloud Console")
        print("3. You have billing enabled (even for free tier)")

print("\n" + "-" * 50)