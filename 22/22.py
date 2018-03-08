from PIL import Image, ImageSequence, ImageDraw


img = Image.open('./white.gif')
new = Image.new('RGB', (200, 200), 'black')
print img.size
newImage = ImageDraw.Draw(new)

x, y = 0, 0

for i in ImageSequence.Iterator(img):
    l, u, r, b = img.getbbox()
    print l, u, r, b
    sx = (l - 100)
    sy = (u - 100)
    x += sx
    y += sy
    if sx == 0 and sy == 0:
        x += 30
        y += 30
    newImage.point((x, y))

new.save('./result.jpg', 'JPEG')