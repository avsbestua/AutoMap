import random
from tkinter.messagebox import showinfo
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from . import constants
from . import functions


def auto_map(prompt, var, map_var):
    random_colors = {}

    mode = var.get()  # AutoMap mode
    map_ = map_var.get()
    print(f'Mode: {mode} Map: {map_}')

    if map_ == "default":
        path = r"./resources/map.png"
        dict_ = constants.countries
    elif map_ == 'flag':
        path = r"./resources/flag_map.png"
        dict_ = constants.countries
    else:
        path = r"./resources/world_map.png"
        dict_ = constants.world_coords

    img = Image.open(path).convert("RGBA")

    text_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(text_layer)

    #ai_answer = functions.ai_request(prompt)  # Requesting information from AI
    print("Got information from AI")


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
                information_ai = str(ai_answer[name])
                color = constants.filling_txt[information_ai]
            except Exception as e:
                information_ai = random.randint(0, 5)
                if map_ == 'default' or map_ == 'world':
                    print(f"Color not found {information_ai} {e}")
                    try:
                        color = random_colors[information_ai]
                        print(f"Color found in random {color}")
                    except KeyError:
                        color = (random.randint(80, 255), random.randint(80, 255), random.randint(80, 255), 255)
                        random_colors[information_ai] = color

        if map_ == 'default' or map_ == 'world':
            for coord in points:
                ImageDraw.floodfill(img, xy=coord, value=color, thresh=50)

        x, y = points[0]

        info = str(information_ai)

        if map_ != 'world':
            if len(info) >= 2:
                x -= 30
            elif len(info) >= 4:
                x -= 70

            if name == 'luxembourg':
                continue  # Next iteration if name in list

            elif name in ['cyprus', 'kosovo',
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

            size += constants.GLOBAL_SIZE_MODIFIER  # Global size modifier fot other fonts. Main font is BIPS

            draw.text((x, y),
                      info,
                      font=ImageFont.truetype(r"./resources/font.ttf", size),
                      fill=(255, 255, 255, 255),
                      stroke_width=15,
                      stroke_fill=(0, 0, 0, 255))

            relief = Image.open(r"./resources/map_relief.png").convert("RGBA")
            relief = relief.resize(img.size)

            r, g, b, a = relief.split()
            new_alpha = a.point(lambda p: int(p * 0.3))
            relief.putalpha(new_alpha)

            result = Image.alpha_composite(img, relief)

            borders = Image.open(r'./resources/map.png').convert("RGBA")  # Second borders layer
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

            result.save(r".\img.png")

        else:

            size = 50
            size += constants.GLOBAL_SIZE_MODIFIER  # Global size modifier fot other fonts. Main font is BIPS

            draw.text((x, y),
                      info,
                      font=ImageFont.truetype(r"./resources/font.ttf", size),
                      fill=(255, 255, 255, 255),
                      stroke_width=15,
                      stroke_fill=(0, 0, 0, 255))

            result = Image.alpha_composite(img, text_layer)

    result.save('img.png')


    showinfo("AutoMap", "Your Map is ready!")
