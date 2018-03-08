# http://www.pythonchallenge.com/pc/hex/ambiguity.html

from PIL import Image, ImageDraw

img = Image.open('./maze.png').getdata()
new = Image.new('RGBA', img.size, 'black')
newImg = ImageDraw.Draw(new)


# 得到第一行的入口位置和最后一行的出口位置
for i in range(img.size[1]):
    if img.getpixel((i, 0))[0] == 0:
        pos = (i, 0)
    if img.getpixel((i, img.size[0] - 1))[0] == 0:
        endpos = (i, img.size[0] - 1)


path = []
wholepath = []
dire = [(1, 0), (0, 1), (-1, 0), (0, -1)]
wall = (255, ) * 4

# 得到路线图
while pos != endpos:
    img.putpixel(pos, wall)
    flag = 0
    newpos = pos
    for i in dire:
        try:
            pp = (pos[0] + i[0], pos[1] + i[1])
            if img.getpixel(pp) != wall:
                flag += 1
                newpos = pp
        except:
            pass
    if flag == 0:
        if path == []:
            path = wholepath.pop()
            continue
        pos = path[0]
        path = []
    elif flag > 1:
        wholepath.append(path)
        path = [pos]
        pos = newpos
    else:
        path.append(pos)
        pos = newpos
else:
    path.append(pos)
    wholepath.append(path)

img = Image.open('./maze.png').getdata()
# [(newImg.point(p)) for i in wholepath for p in i]
# new.save('./test.png')

data = [(img.getpixel(p)[0], new.putpixel(p, wall)) for i in wholepath for p in i]
out = open('./24.zip', 'wb')
for i in data[1::2]:
    out.write(chr(i[0]))

out.close()
new.save('./24.png')