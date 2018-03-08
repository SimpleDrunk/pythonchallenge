# http://www.pythonchallenge.com/pc/return/mozart.html


from PIL import Image


img = Image.open("./mozart.gif")
secret = Image.new('RGB', (640, 480))

for i in range(480):
    for j in range(640):
        if img.getpixel((j, i)) == 195:
            [secret.putpixel((k, i), img.getpixel(( (k+j)%640, i ))) for k in range(640)]
            break

secret.save(r"./secret.jpg", "JPEG")
