# http://www.pythonchallenge.com/pc/ring/grandpa.html

# where am I?

# type thailand, notify 'be more accurate'

# type kosamui, notify 'kohsamui'

# use them for username and password

# GET mandelbrot.gif

# from PIL import Image, ImageDraw
#
#
# ori = Image.open('mandelbrot.gif')
#
# left = 0.34
# top = 0.57
# width = 0.036
# height = 0.027
#
# size = ori.size


from PIL import Image

imgbase = Image.open('mandelbrot.gif')
img = imgbase.copy()
left = 0.34
top = 0.57 + 0.027
width = 0.036
height = 0.027
max = 128
diff = []

for j in range(imgbase.size[1]):
    for i in range(imgbase.size[0]):
        point0 = complex(left + i * width / imgbase.size[0], top - (1+j) * height / imgbase.size[1])
        point = 0 + 0j
        for k in range(max):
            point = point ** 2 + point0
            if point.imag ** 2 + point.real ** 2 > 4:
                break
        img.putpixel((i, j), k)
        if k != imgbase.getpixel((i, j)):
            diff.append(k - imgbase.getpixel((i, j)))

img.save('new.png')
print len(diff)
# print diff
# 1679 = 23 * 73

resimg = Image.new('1', (23, 73))
resimg.putdata([i < 0 for i in diff])
resimg.save('31.jpg')

# Arecibo Message