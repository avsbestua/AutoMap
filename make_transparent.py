from PIL import Image

img = Image.open("img.png").convert("RGBA")
target_color = (88,220,197)

pixels = img.getdata()
new_pixels = []

for pixel in pixels:
    if pixel[:3] == target_color:
        new_pixels.append((pixel[0], pixel[1], pixel[2], 0))
    else:
        new_pixels.append(pixel)

img.putdata(new_pixels)
img.save("result.png")