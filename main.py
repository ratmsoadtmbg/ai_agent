import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

if len(sys.argv) == 1 or sys.argv[1] == "--verbose":
    print("ValueError: Must pass argument for prompt.")
    sys.exit(1)

if len(sys.argv) > 2 and sys.argv[2] != "--verbose":
    print("ValueError: Only one prompt may be entered at a time.")
    sys.exit(1)

load_dotenv()
key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=key)
messages = [
    types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
]

try:
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
    )
except Exception as e:
    print(e)
    sys.exit(1)

print(response.text)
if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
    print(f'User prompt: {sys.argv[1]}')
    print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
    print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
