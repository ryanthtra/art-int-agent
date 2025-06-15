import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

#def main():
if len(sys.argv) != 3:
    print("Usage: python3 main.py <question to ask Gemini> [--verbose]")
    sys.exit(1)

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
user_prompt = sys.argv[1]
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

llm_response = client.models.generate_content(
    model="gemini-2.0-flash-001", 
    contents=messages,
)

print(f"{llm_response.text}")

if sys.argv[2] == "--verbose":
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {llm_response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {llm_response.usage_metadata.candidates_token_count}")

