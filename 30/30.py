# http://www.pythonchallenge.com/pc/ring/yankeedoodle.html

# http://www.pythonchallenge.com/pc/ring/yankeedoodle.csv

# f = open('./yankeedoodle.csv', 'r')
# print f
# print len(f.split())

# len = 7367

# import math
#
# for i in range(2, int(math.sqrt(7367) + 1)):
#     if 7367 % i == 0:
#         print i, 7367 / i

# 7367 = 53 * 139


# from PIL import Image, ImageDraw
# import re
#
# p = re.compile(r'(0.\d*)')
# f = open('yankeedoodle.csv', 'r').read()
# ff = re.findall(p, f)
# print ff
# new = Image.new('RGB', (53, 139), 'black')
# draw = ImageDraw.Draw(new)
#
# for i in range(0, len(ff)):
#     draw.point((i % 53, int(i / 53)), (int(float(ff[i]) * 255), ) * 3)
#
# new.save('30.jpg')

# 图片左右翻转

# from PIL import Image
#
# img = Image.open('30.jpg')
# out = img.transpose(Image.FLIP_LEFT_RIGHT)
# out.save('30a.jpg')


# n = str(x[i])[5] + str(x[i+1])[5] + str(x[i+2])[6]

from PIL import Image, ImageDraw
import re

p = re.compile(r'(0.\d*)')
f = open('yankeedoodle.csv', 'r').read()
ff = re.findall(p, f)

code = [chr(int(ff[i][5] + ff[i+1][5] + ff[i+2][6])) for i in range(0, len(ff)-2, 3)]
print ''.join(code)


# There is lots of room here for a long message, but we only need very little space to say "look at grandpa", so the rest is just garbage.