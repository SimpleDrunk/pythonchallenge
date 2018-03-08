# http://www.pythonchallenge.com/pc/return/italy.html

from PIL import Image

img = Image.open("./wire.png")
secret = Image.new('RGB', (100, 100))

x, y = 0, 0
line = 1
flag = 0
count = 0
max = 99


for count in range(10000):
        secret.putpixel((x, y), img.getpixel((count, 0)))
        if flag == 0:
            x += 1
        elif flag == 1:
            y += 1
        elif flag == 2:
            x -= 1
        else:
            y -= 1

        if line == max:
            flag += 1
            line = 1
            if flag == 4:
                flag = 0
                max -= 2
                x += 1
                y += 1
        else:
            line += 1

        count += 1

secret.save("secret.jpg", "JPEG")