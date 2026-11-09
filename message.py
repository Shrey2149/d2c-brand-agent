from dotenv import load_dotenv
from google import genai 

load_dotenv()
client = genai.Client()
MODEL = "gemini-3.5-flash-lite"

history = [
    {"role": "user",  "parts": [{"text": "Hi, my name is Shrey and I work at a D2C brand."}]},
    {"role": "model", "parts": [{"text": "Nice to meet you, Shrey! How can I help?"}]},
    {"role": "user",  "parts": [{"text": "What is my name and where do I work?"}]},
]

response = client.models.generate_content(model=MODEL, contents=history)
print(response.text)

response = client.models.generate_content(model=MODEL, contents="What is my name and where do I work?")
print(response.text)
