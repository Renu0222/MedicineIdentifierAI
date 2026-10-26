
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("ERROR: API key not found. Check your .env file.")
else:
    try:
        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="qwen/qwen3.8-27b",
            messages=[
                {
                    "role": "user",
                    "content": "Reply with only OK."
                }
            ],
            max_completion_tokens=30,
        )

        print("API connection successful!")
        print("Model response:", response.choices[0].message.content)

    except Exception as error:
        print("API test failed:", type(error).__name__, str(error))
