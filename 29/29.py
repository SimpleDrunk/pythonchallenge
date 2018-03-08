# http://www.pythonchallenge.com/pc/ring/guido.html


import urllib
import bz2

url = 'http://repeat:switch@www.pythonchallenge.com/pc/ring/guido.html'
f = urllib.urlopen(url)
blanks = [chr(len(line) - 1) for line in f.readlines()[12::]]
print blanks
text = ''.join(blanks)
print text

print bz2.decompress(text)
