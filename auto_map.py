from PIL import Image, ImageDraw, ImageFont, ImageFilter
import ai
import constants
import random
import cv2
import numpy as np

img = Image.open(r".\resources\test.png").convert("RGBA")

text_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))
draw = ImageDraw.Draw(text_layer)

#ai_answer = ai.ai_request() #Requesting information from AI

for name, points in constants.countries.items():
    try:
        info = ai_answer[name]
        for (low_lim, high_lim), color_tup in constants.filling.items():
            info = int(info)
            if low_lim <= info <= high_lim:
                color = color_tup
                break
            else:
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)


    except:
        info = random.randint(0, 10)
        color = (random.randint(80, 255), random.randint(80, 255), random.randint(80, 255), 255)

    for coord in points:
        ImageDraw.floodfill(img, xy=coord, value=color, thresh=50)

    x, y = points[0]

    info = str(info)

    if len(info) >= 2:
        x -= 30
    elif len(info) >= 4:
        x -= 70

    if name in ['luxembourg', 'cyprus', 'kosovo',
                'montenegro']:
        continue  # Next iteration if name in list

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
        ,'estonia', 'lithuania', 'north_macedonia', 'switzerland', 'bosnia']:
        y -= 25

    else:
        size = 125

    if len(info) == 1:
        size += 25

    draw.text((x, y),
              info,
              font=ImageFont.truetype(r".\resources\font.ttf", size),
              fill=(255, 255, 255, 255),
              stroke_width=15,
              stroke_fill=(0, 0, 0, 255))

relief = Image.open(r"resources/map_relief.png").convert("RGBA")
relief = relief.resize(img.size)

r, g, b, a = relief.split()
new_alpha = a.point(lambda p: int(p * 0.3))
relief.putalpha(new_alpha)

result = Image.alpha_composite(img, relief)
result = Image.alpha_composite(result, text_layer)

borders = Image.open(r'resources/test.png').convert("RGBA") #Second borders layer
borders = borders.resize(result.size)

borders = np.array(borders)

borders = cv2.GaussianBlur(borders, (13, 13), sigmaX=16)
borders = Image.fromarray(borders)
borders.save("fwwffwf.png")
result = Image.alpha_composite(result, borders)

result.save(r".\img.png")