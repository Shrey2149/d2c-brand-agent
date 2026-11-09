from dotenv import load_dotenv
from google import genai 
from google.genai import types

load_dotenv()
client = genai.Client()
MODEL = "gemini-3.5-flash-lite"

history = []
print("Chat started. Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if(user_input.lower() == "exit"):
        break

    history.append({"role": "user", "parts": [{"text": user_input}]})

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=history,
            config=types.GenerateContentConfig(
                system_instruction="You are a helpful assistant for a D2C clothing brand. Keep answers short."
            ),
        )

    except Exception as e:
        print("AI: Sorry, the server is busy. Please send that again.\n")
        history.pop()   
        continue 

    reply = response.text
    print("AI:", reply, "\n")

    history.append({"role": "model", "parts": [{"text": reply}]})

print(f"Chat ended. The conversation had {len(history)} messages.")


