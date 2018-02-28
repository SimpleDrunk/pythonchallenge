from PIL import Image


def eleven():
    img = Image.open("./cave.jpg")
    even = Image.new("RGB", (320, 480))
    odd = Image.new("RGB", (320, 480))

    flag = 0
    for y in range(0, 480):
        for x in range(0, 640):
            if x % 2 == flag:
                even.putpixel((x / 2, y), img.getpixel((x, y)))
            else:
                odd.putpixel((x / 2, y), img.getpixel((x, y)))
        if flag == 1:
            flag = 0
        else:
            flag = 1

    even.save("d:/even.jpg", "JPEG")
    odd.save("d:/odd.jpg", "JPEG")


eleven()