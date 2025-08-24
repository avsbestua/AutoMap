import json
import requests

url = "https://openrouter.ai/api/v1/chat/completions"


def ai_request(prompt):
    with open(r"./map/tk.txt", 'r') as file:
        API_KEY = file.read()

    print(prompt)
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek/deepseek-r1-0528:free", #moonshotai/kimi-k2:free
        "messages": [
            {"role": "system",
             "content": "You are an assistant. You must provide accurate answers and may use the internet to search for information."},
            {"role": "user", "content": f"""Fill in a dictionary where the key """ + str(prompt) + """
    Search the internet and return the result as JSON. Dont write 'json' in start

    If there is no exact data for a country, use the average value from all other countries.

    Provide the answer only as a dictionary, without explanations.

    {
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
        "luxembourg":,
        "netherlands":,
        "united_kingdom":,
        "ireland":,
        "iceland":,
        "serbia":,
        "belgium":,
        "usa":
    }
    """}
        ],
        "temperature": 0.5,
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        res = result['choices'][0]['message']['content'].strip()
        try:
            # Пробуємо перетворити текст у словник
            country_dict = json.loads(res)
            return country_dict
        except json.JSONDecodeError:
            print("Failed to convert into dictionary")
            print("Result:", res)
            return None
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
