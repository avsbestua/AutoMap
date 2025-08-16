import requests
import json

url = "https://openrouter.ai/api/v1/chat/completions"


def ai_request():
    with open("token.txt", 'r') as file:
        API_KEY = file.read()

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "moonshotai/kimi-k2:free",
        "messages": [
            {"role": "system", "content": "You are an assistant. You must provide accurate answers and may use the internet to search for information."},
            {"role": "user", "content": """Fill in a dictionary where the key is does Volodymyr Zeleskyi was in your country, write "Yes" or "No" you must write for example if 1000 write 1k, if 1 million, write 1m
    Search the internet and return the result as JSON. IT MUST BE JSON format. Dont write anything else

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
        "belgium":
    }
    """}
        ],
        "temperature": 0.7,
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
            print("Не вдалося перетворити відповідь у словник.")
            print("Отримана відповідь:", res)
            return None
    else:
        print(f"Помилка: {response.status_code} - {response.text}")
        return None
