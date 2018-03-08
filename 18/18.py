# http://www.pythonchallenge.com/pc/return/balloons.html

# brightness

# down delta.gz and open

import difflib


f = open('delta.txt', 'r')
content = f.read()
f.close()

lines = content.splitlines()
first, second = [], []
for line in lines:
    first.append(line[:53])
    second.append(line[56:])

diff = list(difflib.ndiff(first, second))

img = ['', '', '']

for item in diff:
    bytes = [chr(int(byte, 16)) for byte in item[2:].split()]
    if item[0] == ' ':
        img[0] += ''.join(bytes)
    elif item[0] == '+':
        img[1] += ''.join(bytes)
    elif item[0] == '-':
        img[2] += ''.join(bytes)


for i in range(3):
    open('secret%d.jpg' % i, 'wb').write(img[i])

