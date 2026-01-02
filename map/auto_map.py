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


import sys

if sys.platform == 'win32':
    # Windows specific imports
    import random
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
    from . import constants
    from . import functions
    from tkinter.messagebox import askyesno, showwarning, showerror
    from pathlib import Path

elif sys.platform == 'darwin':  #@TODO Make universal imports
    # macOS specific imports
    import random
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
    from . import constants
    from . import functions
    from tkinter.messagebox import showwarning, showerror
    from pathlib import Path

def auto_map(prompt, mode, map_, size_mod, optional_feature, model, font_name):
    #Most least and short form conflict solution @TODO Make most/least and short form compatible 
    
    if optional_feature == "short_form":
        prompt += " Write in short form, for example 1000=1k, 1000000=1M etc."
    
    if optional_feature == "short_form" and mode == "num":
        showwarning("Warning", "Short form feature is only available for text mode. It will be disabled.")
        optional_feature = None

    if optional_feature == "most_least" and mode == "text":
        showwarning("Warning", "Most/least feature may be incompatible with text mode.")

    if optional_feature == "most_least" and map_ == "world":
        showwarning("Warning", "Most/Least feature is not available for world map. It will be disabled.")
        optional_feature = None

    random_colors = {}
                         
    print(f'Mode: {mode} Map: {map_} Model: {model}')
# map selecting
    if map_ == "default":
        path = Path(__file__).parent.parent / "./resources/maps/default_map.png"
        dict_ = constants.countries
    elif map_ == 'flag':
        path = Path(__file__).parent.parent / "./resources/maps/flag_map.png"
        dict_ = constants.countries
    elif map_ == 'world':
        path = Path(__file__).parent.parent / "./resources/maps/world_map.png"
        dict_ = constants.world_coords
# opening selected map
    img = Image.open(path).convert("RGBA")

    text_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(text_layer)
    
# Requesting information from AI
    ai_answer = functions.ai_request(prompt, map_, model)

    if ai_answer is None:
        showerror("Error", "No information or bad info received from AI")
        return
    
    print("Got information from AI")

    if optional_feature == "most_least":
        most_least = Image.new("RGBA", img.size, (255, 255, 255, 0))
        ml_draw = ImageDraw.Draw(most_least)
        '''Writing the most and the least country'''
        most_country = max(ai_answer, key=ai_answer.get)
        least_country = min(ai_answer, key=ai_answer.get)

        ml_draw.text((106, 1240),
                f'Most: {most_country.capitalize()}\nLeast: {least_country.capitalize()}',
                font=ImageFont.truetype(str(Path("resources/fonts") / font_name), 150),
                fill=(255, 255, 255, 255),
                stroke_width=15,
                stroke_fill=(0, 0, 0, 255))

    for name, points in dict_.items():
        '''Number mode'''
        if mode == 'num':
            try:
                color = (random.randint(80, 255), random.randint(80, 255), random.randint(80, 255), 255)
                info = ai_answer[name]
                for (low_lim, high_lim), color_tup in constants.filling_num.items():
                    info = int(info)
                    if low_lim <= info <= high_lim:
                        color = color_tup
                        break
            except KeyError as e:
                print(f"One missing color {e}")
                print(info, name)
                color = (random.randint(80, 255), random.randint(80, 255), random.randint(80, 255), 255)
                random_colors[info] = color


        elif mode == 'txt':
            '''Text mode'''
            try:
                info = str(ai_answer[name])
                color = constants.filling_txt[info]
            except Exception as e:
                if map_ == 'default' or map_ == 'world':
                    print(f"Color not found {info} {e}")
                    try:
                        color = random_colors[info]
                        print(f"Color found in random {color}")
                    except KeyError:
                        color = (random.randint(80, 255), random.randint(80, 255), random.randint(80, 255), 255)
                        random_colors[info] = color
# filling
        if map_ == 'default' or map_ == 'world':
            for coord in points:
                ImageDraw.floodfill(img, xy=coord, value=color, thresh=50)

        x, y = points[0]

        try:
            info = str(info)
        except UnboundLocalError:
            print(f'No information for {name}')
            continue

        if map_ == 'flag' or map_ == 'default':
            if len(info) >= 2:
                x -= 30
            elif len(info) >= 4:
                x -= 70
# number in countries

            if name in ['cyprus', 'kosovo',
                          'montenegro']:
                size = 70

            elif name in ['ukraine', 'poland', 'france',
                          'spain',
                          'turkey', 'romania', 'italy', 'belarus', 'united_kingdom', 'germany']:
                size = 175
            elif name in ['sweden', 'norway', 'finland']:
                size = 100

            elif name in ['russia', 'usa']:
                y -= 10
                size = 250
            elif name in ['slovenia', 'latvia', 'lithuania', 'estonia', 'switzerland', 'austria', 'slovakia', 'hungary',
                          'croatia', 'netherlands', 'belgium', 'czechia', 'moldova', 'bosnia_and_herzegovina', 'serbia',
                          'bulgaria', 'albania', 'greece', 'ireland', 'iceland', 'norway', 'finland', 'sweden', 'denmark',
                          'portugal']:
                size = 70
            elif name in ['ireland', 'belgium'
                , 'estonia', 'lithuania', 'north_macedonia', 'switzerland', 'bosnia']:
                y -= 25

            else:
                size = 125

            if len(info) == 1:
                y -= 20
                size += 25

            size += size_mod  # Global size modifier fot other fonts. Main font is BIPS

            draw.text((x, y),
                      info,
                      font=ImageFont.truetype(str(Path("resources/fonts") / font_name), size),
                      fill=(255, 255, 255, 255),
                      stroke_width=15,
                      stroke_fill=(0, 0, 0, 255))


        else:

            size = 50
            size += size_mod  # Global size modifier fot other fonts. Main font is BIPS

            draw.text((x, y),
                      info,
                      font=ImageFont.truetype(str(Path("resources/fonts") / font_name), size),
                      fill=(255, 255, 255, 255),
                      stroke_width=15,
                      stroke_fill=(0, 0, 0, 255))


# adding relief map
    if map_ in ['default', 'flag']:
        relief = Image.open(Path(__file__).parent.parent / "./resources/maps/map_relief.png").convert("RGBA")
        relief = relief.resize(img.size)

        r, g, b, a = relief.split()
        new_alpha = a.point(lambda p: int(p * 0.3))
        relief.putalpha(new_alpha)

        result = Image.alpha_composite(img, relief)

        borders = Image.open(Path(__file__).parent.parent / "./resources/maps/default_map.png").convert("RGBA")  # Second borders layer
        borders = borders.resize(result.size)

        borders = borders.filter(ImageFilter.GaussianBlur(radius=15))

        pixels = borders.load()
        for x in range(borders.width):
            for y in range(borders.height):
                r, g, b, a = pixels[x, y]

                if r != 0 and g != 0 and b != 0:
                    pixels[x, y] = (0, 0, 0, a if a == 0 else a + 30)

        result = Image.alpha_composite(result, borders)
        result = Image.alpha_composite(result, text_layer)

        if optional_feature == "most_least" and map_ != "world": # Adding most and least layer if flag is set
            result = Image.alpha_composite(result, most_least)

# merging layers
    elif map_ == 'world':
        result = Image.alpha_composite(img, text_layer)

    result.save(Path(__file__).parent.parent / "result.png")
    print("Map saved as result.png")
    result.show("Map")