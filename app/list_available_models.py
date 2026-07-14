"""
This script lists all available models for your Google API key
"""
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("ERROR: GOOGLE_API_KEY not found in .env file")
    exit(1)

print(f"API Key: {api_key[:20]}...")
print("=" * 70)

try:
    # Configure the API
    genai.configure(api_key=api_key)
    
    print("\nFetching available models...")
    print("-" * 70)
    
    # List all available models
    models = genai.list_models()
    models_list = list(models)
    
    print(f"\nFound {len(models_list)} models:\n")
    
    for i, model in enumerate(models_list, 1):
        print(f"{i}. Model Name: {model.name}")
        print(f"   Display Name: {model.display_name}")
        print(f"   Description: {model.description[:100] if model.description else 'N/A'}...")
        print(f"   Supported Methods: {', '.join(model.supported_actions) if hasattr(model, 'supported_actions') else 'N/A'}")
        print()
    
    print("=" * 70)
    print("\nRECOMMENDATION:")
    print("Look for models with 'generateContent' in supported methods")
    print("Common free tier models: gemini-1.5-flash, gemini-1.5-pro, gemini-pro")
    
except Exception as e:
    print(f"\nERROR: {e}")
    print("\n" + "=" * 70)
    print("TROUBLESHOOTING STEPS:")
    print("=" * 70)
    print("1. Go to: https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com")
    print("2. Click ENABLE and wait 2-3 minutes")
    print("3. Go to: https://makersuite.google.com/app/apikey")
    print("4. CREATE A NEW API KEY (old keys won't work)")
    print("5. Update app/.env with the new key")
    print("6. Enable billing at: https://console.cloud.google.com/billing")
    print("=" * 70)