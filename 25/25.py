# http://www.pythonchallenge.com/pc/hex/lake.html

# http://www.pythonchallenge.com/pc/hex/lake1-25.wav

# import urllib
# for count in range(1, 26):
#     url = "http://butter:fly@www.pythonchallenge.com/pc/hex/lake%d.wav" % count
#     urllib.urlretrieve(url, 'lake%d.wav' % count)


import wave
from PIL import Image

f = wave.open('lake1.wav', 'rb')
new = []

for i in range(1, 26):
    f = wave.open('lake%d.wav' % i, 'rb')
    new.append(Image.frombytes('RGB', (60, 60), f.readframes(f.getnframes())))


total = Image.new('RGB', (300, 300))
for i in range(25):
    total.paste(new[i], ((i % 5) * 60, (i / 5)*60))

total.save('./25.jpg')
