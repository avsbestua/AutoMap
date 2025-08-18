from PIL import Image, ImageDraw, ImageFont, ImageFilter
import ai
import constants
import random

img = Image.open(r".\resources\map.png").convert("RGBA")
img = img.filter(ImageFilter.GaussianBlur(radius=0.9))
draw = ImageDraw.Draw(img)

ai_answer = ai.ai_request() #Requesting information from AI

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

img = img.filter(ImageFilter.GaussianBlur(radius=0.5))
img.save(r".\img.png")
