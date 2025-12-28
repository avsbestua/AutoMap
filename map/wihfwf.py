from google import genai
import os

with open(r"./map/google_tk.txt", 'r') as file:
    os.environ['GEMINI_API_KEY'] = file.read().strip()

client = genai.Client()
request = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Can you use information from the internet?",
)

print("AI response:", request.text)