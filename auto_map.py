import random

from PIL import Image, ImageDraw, ImageFont
import constants, ai

img = Image.open(r".\map.png").convert("RGBA")
draw = ImageDraw.Draw(img)
fills = {}

ai_answer = ai.ai_request() #Requesting information from AI

for name, points in constants.countries.items():
    try:
        info = ai_answer[name]
        fills[info] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)
        color = fills[info]
    except:
        info = ''

        continue

    for coord in points:
        ImageDraw.floodfill(img, xy=coord, value=color, thresh=200)


    x, y = points[0]

    if name in ['luxembourg', 'cyprus', 'kosovo',
                'slovenia', 'montenegro']:
        continue #Next iteration if name in list

    elif name in ['ukraine', 'poland', 'france',
                'spain', 'finland',
                'turkey', 'romania', 'italy']:
        size = 35
        x -= 15; y += 10

    elif name in ['parasha']:
        size = 67

    elif name in ['germany', 'sweden', 'united_kingdom',
                  'belarus']:
        x += 8
        size = 25
    else:
        size = 15

    draw.text((x,y), str(info), font=ImageFont.truetype(r".\BIPs.ttf", size), fill=(0, 0, 0, 255))

img.save(r".\img.png")