# Copyright 2025-2026 Avsbest
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
from google import genai
from tkinter.messagebox import showerror
from dotenv import load_dotenv

load_dotenv(".env") #loading .env file

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
def ai_request(prompt: str, mode: str, ai_model: str):
    if mode == 'default' or mode == 'flag':
        dict_ = europe
    elif mode == 'world':
        dict_ = world

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
            model=ai_model,
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
        try:
            json_style = request.text.strip().replace("```python", "").replace("```", "").strip()
            country_dict = json.loads(json_style)
            return country_dict

        except json.JSONDecodeError:
            showerror("Error", f"Failed to convert into dictionary. Result {json_style}")
            print("Result:", json_style)
            return None



