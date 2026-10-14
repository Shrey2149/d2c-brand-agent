from dotenv import load_dotenv
from google.genai import types
from google import genai

load_dotenv()
client = genai.Client(
    http_options=types.HttpOptions(retry_options=types.HttpRetryOptions(attempts=5))
)
# for m in client.models.list():
#     print(m.name)

response = client.models.generate_content(
    model = "gemini-3.5-flash-lite",
    contents = "Explain what a D2C brand is in one sentence.",
)
print(response.text)