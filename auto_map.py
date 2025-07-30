from PIL import Image, ImageDraw, ImageFont
import constants, ai, random

img = Image.open(r".\map2.png").convert("RGB")
draw = ImageDraw.Draw(img)

#ai_answer = ai.ai_request() #Requesting information from AI
# if constants.text_mode:
#     countries = constants.countries_text
# else:
#     countries = constants.countries

for name, points in constants.countries.items():
    try:
        # info = ai_answer[name]
        # for (low_lim, high_lim), color_tup in constants.filling.items():
        #     info = int(info)
        #     if low_lim <= info <= high_lim:
        #         color = color_tup
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        info = random.randint(0, 5)
    except:
        pass


    for coord in points:
        ImageDraw.floodfill(img, xy=coord, value=color, thresh=50)


    x, y = points[0]

    if name in ['luxembourg', 'cyprus', 'kosovo',
                'slovenia', 'montenegro']:
        continue #Next iteration if name in list

    elif name in ['ukraine', 'poland', 'france',
                'spain', 'finland',
                'turkey', 'romania', 'italy' ,'norway' , 'belarus' , 'sweden' , 'united_kingdom' , 'iceland' , 'germany']:
        size = 75


    elif name in ['russia']:
        size = 120

    elif name in ['ireland', 'denmark', 'belgium',
                  'netherlands', 'latvia', 'estonia', 'lithuania', 'czechia', 'slovakia', 'austria', 'hungary', 'switzerland' , 'bulgaria']:
        size = 40

    else:
        size = 30

    draw.text((x,y), str(info), font=ImageFont.truetype(r".\BIPs.ttf", size), fill=(0, 0, 0, 255))

img.save(r".\img.png")