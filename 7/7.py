from PIL import Image
import re

f = Image.open("./oxygen.png", 'r')
p = re.compile("\d+")

res = ""

for i in range(0, 608, 7):
    pix = f.getpixel((i, 0))
    res += chr(int(pix[0]))

print res
li = re.findall(p, res)
print "".join([chr(int(x)) for x in li])