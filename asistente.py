import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

print("Assistent acadèmic iniciat. Escriu 'sortir' per acabar.\n")

while True:
    pregunta = input("Tu: ")
    
    if pregunta.lower() == "sortir":
        print("Fins aviat!")
        break
    
    if not pregunta.strip():
        continue
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=pregunta
        )
        print(f"Assistent: {response.text}\n")
    except Exception as e:
        print