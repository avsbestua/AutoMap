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
from tkinter.messagebox import showerror

from dotenv import load_dotenv
from google import genai
from pathlib import Path

from . import constants
from ast import literal_eval

load_dotenv(".env")  # loading .env file

# mode selecting
def ai_request(prompt: str, mode: str, ai_model: str):
    if mode == 'default' or mode == 'flag':
        dict_ = constants.europe
    elif mode == 'world':
        dict_ = constants.world

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


def load_filling():

    path = Path(__file__).parent / "filling.json"

    filling_txt = {}
    filling_num = {}

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)


        raw_txt = data.get("filling_txt", {})
        filling_txt = {k: tuple(v) for k, v in raw_txt.items()}


        raw_num = data.get("filling_num", {})
        for key_str, color_list in raw_num.items():
            try:
                tuple_key = literal_eval(key_str)
                filling_num[tuple_key] = tuple(color_list)
            except (ValueError, SyntaxError):
                print(f"Invalid JSON Key (see docs): {key_str}")

    except Exception as e:
        showerror("Error!", f"JSON reading error {e}")

    return filling_txt, filling_num