import json
import requests
import os
from google import genai
from tkinter.messagebox import showerror
from pathlib import Path

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
    with open(Path(__file__).parent / "tk.txt", 'r') as file:
        os.environ['GEMINI_API_KEY'] = file.read().strip()
        
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
    try:
        request = client.models.generate_content(
            model=AI_MODEL,
            contents=prompt_to_ai,
        )


    except Exception as e:
        showerror("Error", f"AI request failed: {e}")
        return None

    try:
        json_style = request.text.strip().replace("```json", "").replace("```", "").strip()
        country_dict = json.loads(json_style)
        return country_dict
    except json.JSONDecodeError:
        showerror("Error", f"Failed to convert into dictionary. Result {json_style}")
        print("Result:", json_style)
        return None



