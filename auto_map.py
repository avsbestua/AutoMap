from PIL import Image, ImageDraw, ImageFont
import constants, random

img = Image.open(r".\map.png").convert("RGBA")
draw = ImageDraw.Draw(img)


for name, points in constants.countries.items():
    try:
        # info = constants.information[name]
        # color = constants.filling[info]
        pass
    except:
        # info = ''
        # color = (255, 255, 255, 255)
        # continue
        pass
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)
    info = ""
    for coord in points:
        ImageDraw.floodfill(img, xy=coord, value=color, thresh=250)

    if name in ['luxembourg', 'cyprus', 'kosovo', 'slovenia']:
        continue #Next iteration if name in list

    if name in ['ukraine', 'poland', 'germany', 'france',
                'spain', 'parasha', 'finland', 'sweden',
                'turkey', 'romania','italy',]:
        size = 60
    else:
        size = 25

    x,y = points[0]

    draw.text((x,y), str(info), font=ImageFont.truetype(r".\BIPs.ttf", size), fill=(0, 0, 0, 255))

img.save(r".\img.png")