import json
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()
MODEL = "gemini-3.5-flash-lite"

class Product(BaseModel):
    name: str
    category: str
    price: int
    fabric: str

response = client.models.generate_content(
    model = MODEL,
    contents = "Create 5 clothing products for an Indian D2C fashion brand.",
    config = types.GenerateContentConfig(
        response_mime_type = "application/json",
        response_schema = list[Product],
    ),
)

print("RAW TEXT FROM MODEL:")
print(response.text)

products = [Product(**item) for item in json.loads(response.text)]

print("\nVALIDATED PRODUCTS:")
for p in products:
    print(f"{p.name} | {p.category} | ₹{p.price} | {p.fabric}")

