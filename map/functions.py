import json
import requests
import os
from google import genai
from tkinter.messagebox import showerror

url = "https://openrouter.ai/api/v1/chat/completions"
# Europe countries dictionary
europe = """{

        "ukraine":,
        "poland":,
        "moldova":,
        "belarus":,
        "russia":,
        "lithuania":,
        "latvia":,
        "estonia":,
        "finland":,
        "norway":,
        "sweden":,
        "denmark":,
        "germany":,
        "czechia":,
        "slovakia":,
        "austria":,
        "hungary":,
        "switzerland":,
        "slovenia":,
        "romania":,
        "bulgaria":,
        "croatia":,
        "bosnia_and_herzegovina":,
        "montenegro":,
        "north_macedonia":,
        "kosovo":,
        "albania":,
        "greece":,
        "turkey":,
        "cyprus":,
        "portugal":,
        "spain":,
        "italy":,
        "france":,
        "netherlands":,
        "united_kingdom":,
        "ireland":,
        "iceland":,
        "serbia":,
        "belgium":,
        "usa":
    }"""
# Continents dictionary
world ="""{

        "asia":,
        "europe":,
        "australia":,
        "north_america":,
        "south_america":,
        "africa":
    }"""

# mode selecting
def ai_request(prompt: str, mode: str, AI_MODEL: str) -> dict:
    if mode == 'default' or mode == 'flag':
        dict_ = europe
    elif mode == 'world':
        dict_ = world
# reading token from file 
    with open(r"./map/tk.txt", 'r') as file:
        API_KEY = file.read()

    with open(r"./map/google_tk.txt", 'r') as file:
        os.environ['GEMINI_API_KEY'] = file.read()

    print(prompt)

# request data
    prompt_to_ai = f"""Fill in a dictionary where the key """ + str(prompt) + f"""
    Search the internet and return the result as JSON. Dont write 'json' in start

    If there is no exact data for a country or continent, use the approximate value.
             
    Provide the answer only as a dictionary, without explanations.

    Dont include luxembourg
                      
    {dict_}
    """

    client = genai.Client()
    request = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt_to_ai,
    )

    print("AI response:", request.text)

    try:
        json_style = request.text.strip().replace("```json", "").replace("```", "").strip()
        country_dict = json.loads(json_style)
        return country_dict
    except json.JSONDecodeError:
        showerror("Error", f"Failed to convert into dictionary. Result")
        print("Result:", json_style)
        return None


# # request
#     response = requests.post(url, headers=headers, json=data)

#     if response.status_code == 200:
#         result = response.json()
#         res = result['choices'][0]['message']['content'].strip()
#         try:
# # trying to parse dictionary

#     else:
#         showerror("Error", f"Error: {response.status_code} - {response.text}")
#         print(f"Error: {response.status_code} - {response.text}")
        
#         return None
