from PIL import Image, ImageDraw, ImageFont
import constants, ai, random

img = Image.open(r".\map.png").convert("RGBA")
draw = ImageDraw.Draw(img)

ai_answer = ai.ai_request() #Requesting information from AI

for name, points in constants.countries.items():
    try:
        info = ai_answer[name]
        for (low_lim, high_lim), color_tup in constants.filling.items():
            info = int(info)
            if low_lim <= info <= high_lim:
                color = color_tup

    except:
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)

        continue

    for coord in points:
        ImageDraw.floodfill(img, xy=coord, value=color, thresh=170)


    x, y = points[0]

    if name in ['luxembourg', 'cyprus', 'kosovo',
                'slovenia', 'montenegro']:
        continue #Next iteration if name in list

    elif name in ['ukraine', 'poland', 'france',
                'spain', 'finland',
                'turkey', 'romania', 'italy' ,'norway']:
        size = 35
        x -= 15; y += 10

    elif name in ['russia']:
        size = 67

    elif name in ['germany', 'sweden', 'united_kingdom',
                  'belarus']:
        x += 8
        size = 25
    else:
        size = 15

    draw.text((x,y), str(info), font=ImageFont.truetype(r".\BIPs.ttf", size), fill=(0, 0, 0, 255))

img.save(r".\img.png")