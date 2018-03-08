# http://www.pythonchallenge.com/pc/ring/bell.html


# from PIL import Image
#
# img = Image.open('./bell.png')
# new1, new2, new3 = Image.new('RGB', img.size), Image.new('RGB', img.size), Image.new('RGB', img.size)
#
# green = []
#
# for i in range(img.size[1]):
#     for j in range(img.size[0]):
#         new1.putpixel((j, i), (img.getpixel((j, i))[0], 0, 0))
#         new2.putpixel((j, i), (0, img.getpixel((j, i))[1], 0))
#         new3.putpixel((j, i), (0, 0, img.getpixel((j, i))[2]))
#         print img.getpixel((j, i))[1]

# new1.save('1.jpg')
# new2.save('2.jpg')
# new3.save('3.jpg')


from PIL import Image, ImageDraw

img = Image.open('bell.png')
new = Image.new('RGB', img.size, 'black')
newImg = ImageDraw.Draw(new)


r, g, b = img.split()

gdata = list(g.getdata())
newlist = [(gdata[i], gdata[i+1]) for i in range(0, len(gdata), 2)]

for i in newlist:
    newImg.point((i))

new.save('line.jpg')

str = ''
for i in newlist:
    if i[0] - i[1] != 42 or i[0] - i[1] != -42:
        str += chr(abs(i[0]-i[1]))

print str

# whodunnit().split()[0]
# who done it?
# Guido van Rossum
