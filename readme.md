# AutoMap

---

![Logo](resources/demo/banner.png)
`AutoMap` — is an ultimate map creating tool. With `AM` you can create maps by simple mouse pressing.

## Features

---

![GUI](resources/demo/app.png)
`AutoMap` has different options. There is Default Map, Flag map and World map. Here is map example *(Default map)*

![GUI](resources/demo/map_example.png)

## Stack

---
There are libraries we are currently using:

- AI
    - [google-genai](https://github.com/googleapis/python-genai)
- Drawing
    - [pillow](https://github.com/python-pillow/Pillow)
- GUI
    - tkinter
    - [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
- Other
    - [dotenv](https://github.com/theskumar/python-dotenv)

## Installation

---

To get started with **AutoMap**, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/avsbestua/auto_map.git
   cd automap
2. **Set up a virtual environment**
    ```bash
    python -m venv venv
    venv\Scripts\activate # On macOS and Linux: source venv/bin/activate
3. **Installing dependencies**
    ```bash
    pip install -r requirements.txt # On macOS and Linux can be pip3 install -r requirements.txt
4. **Environment Set up**
   The project uses a `.env` file for API keys.
    - Copy the template file:
    - You can get `GEMINI_API_KEY` [here](https://aistudio.google.com/api-keys)
    - Open `.env` and replace the placeholder values with your actual API keys.

## Fonts
AutoMap has 4 default fonts. You can add your own fonts in `resources/fonts` and use them on maps.
![fonts](resources/demo/fonts_gui.png)
![fonts](resources/demo/fonts.png)

## Filling
You can define colors for data in `constants.py` file. Here 2 `dicts`. `filling_txt` defines filling in `Text` mode, for example if data is `Tea` color will be `(246, 255, 0, 255)` ***AutoMap uses RGBA. Last number must be 255.***
`filling_num` defines filling in `Number` mode, for example `if data > 100 and data <= 200` color will be `(235, 40, 33, 255)`
````python
filling_txt = {
    "Tea": (246, 255, 0, 255),
    "Cofe": (54, 4, 4, 255),
}

filling_num = {
    (100, 200): (235, 40, 33, 255),
}
````

## License

---

This project is licensed under the **Apache License 2.0**.

Copyright © 2025-2026 **Avsbest**.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.