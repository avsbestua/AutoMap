from PIL import Image, ImageDraw, ImageFont
import constants

img = Image.open(r"D:\PythonProject1\auto_map\map.png").convert("RGBA")
draw = ImageDraw.Draw(img)


for name, points in constants.countries.items():
    try:
        info = constants.information[name]
        color = constants.filling[info]
    except:
        info = ''
        # color = (255, 255, 255, 255)
        continue

    for coord in points:
        ImageDraw.floodfill(img, xy=coord, value=color, thresh=200)

    if name in ['luxembourg', 'cyprus', 'kosovo', 'slovenia']:
        continue #Next iteration if name in list

    if name in ['ukraine', 'poland', 'germany', 'france',
                'spain', 'parasha', 'finland', 'sweden',
                'turkey', 'romania']:
        size = 60
    else:
        size = 25

    x,y = points[0]

    draw.text((x,y), str(info), font=ImageFont.truetype(r"D:\PythonProject1\auto_map\BIPs.ttf", size), fill=(0, 0, 0, 255))

img.save(r"D:\PythonProject1\auto_map\img.png")