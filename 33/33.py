# http://www.pythonchallenge.com/pc/rock/beer.html


from PIL import Image
import math

im = Image.open('beer2.png')
colors = im.getcolors()
data = im.getdata()

for i in range(65, -1, -2):
    s = []
    t = []
    for f in data:
        if f != colors[i][1] and f != colors[i-1][1]:
            s.append(f)
            t.append(0)
        else:
            if f == colors[i][1]:
                t.append(1)
            else:
                t.append(0)
    data = s
    n = int(math.sqrt(len(t)))
    new = Image.new('1', (n, n))
    new.putdata(t)
    new.save('%d.png' % ((i-1) / 2))


# http://www.pythonchallenge.com/pc/rock/gremlins.html

# ******************** E    N    D *********************


