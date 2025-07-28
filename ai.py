import requests
import json

API_KEY = "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"
url = "https://openrouter.ai/api/v1/chat/completions"


def ai_request():
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "moonshotai/kimi-k2:free",
        "messages": [
            {"role": "system", "content": "Ти помічник."},
            {"role": "user", "content": """Заповни словник, де ключ — країна, а значення — приблизна кількість університетів у цій країні.

    Якщо точних даних по країні немає, підстав середнє значення серед усіх інших.

    Відповідь дай тільки у вигляді словника, без пояснень.

    {
        "ukraine":,
        "poland":,
        "moldova":,
        "belarus":,
        "parasha":,
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
