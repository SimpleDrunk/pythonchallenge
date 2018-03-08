# -*- coding:utf-8 -*-

#  http://www.pythonchallenge.com/pc/hex/idiot2.html

# import urllib, re
#
#
# url = "http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg"
# find = re.compile(r'bytes \d*-(\d*)')
# # F12 Network -> Headers -> Content-Range
# # 0-30202/2123456789
# start = 30202
# end = 2123456789
#
# while start < end:
#     opener = urllib.FancyURLopener()
#     opener.addheader('Range', 'bytes=%d-%d' % (start, end))
#     f = opener.open(url)
#     start = re.findall(find, str(f.info()))
#     print start
#     print f.info()
#     if len(start) > 0:
#         start = int(start[0] + 1)
#
# open(r'.\out20.zip', 'wb').write(f.read())

# import urllib, re
# url = 'http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg'
# start = 30203
# end = 2123456789
# find = re.compile(r'bytes \d*-(\d*)')
# r = []
# r.append(start)
# while start < end:
#     opener = urllib.FancyURLopener()
#     opener.addheader('Range', 'bytes=%d-%d' % (start, end))
#     f = opener.open(url)
#     start = re.findall(find, str(f.info()))
#     if len(start) > 0:
#         r.append(int(start[0]))
#         start = int(start[0])+1
#     print f.read()
#     if start >= end:
#         open(r'.\out20.zip','wb').write(f.read())
#
# print r

# Why don't you respect my privacy?
# we can go on in this way for really long time.
# stop this!
# invader! invader!
# ok, invader. you are inside now.
# [30203, 30236, 30283, 30294, 30312, 30346]

# http://www.pythonchallenge.com/pc/hex/invader.html
# not helpful

# import urllib, re
# url = 'http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg'
# start = 2123456789
# find = re.compile(r'bytes \d*-(\d*)')
# opener = urllib.FancyURLopener()
# opener.addheader('Range', 'bytes=%d-%d' % (start, pow(2, 31)))
# f = opener.open(url)
# print f.read()
# print f.info()

# esrever ni emankcin wen ruoy si drowssap eht
# Content-Type: application/octet-stream
# Content-Transfer-Encoding: binary
# Content-Range: bytes 2123456744-2123456788/2123456789
# Content-Length: 45
# Connection: close
# Date: Tue, 06 Mar 2018 02:59:46 GMT
# Server: lighttpd/1.4.35

# invader --> redavni
# 2123456744 --> 2123456743, 2123456789?
# 2123456743 --> 2123456789?

# import urllib, re
# url = 'http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg'
# start = 2123456743
# end = 2123456789
# find = re.compile(r'bytes \d*-(\d*)')
# opener = urllib.FancyURLopener()
# opener.addheader('Range', 'bytes=%d-%d' % (start, end))
# f = opener.open(url)
# print f.read()
# print f.info()

# and it is hiding at 1152983631.
#
# Content-Type: application/octet-stream
# Content-Transfer-Encoding: binary
# Content-Range: bytes 2123456712-2123456743/2123456789
# Content-Length: 32
# Connection: close
# Date: Tue, 06 Mar 2018 03:04:19 GMT
# Server: lighttpd/1.4.35


import urllib


url = 'http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg'
start = 1152983631
# end = 2123456789
end = 1153223363
opener = urllib.FancyURLopener()
opener.addheader('Range', 'bytes=%d-%d' % (start, end))
f = opener.open(url)
print f.info()
# print f.read()
open(r'./20.zip', 'wb').write(f.read())

# ['P', 'K', '\x03', '\x04', '\x14', '\x00', '\t', '\x00', '\x08', '\x00']
# PK\x03\x04 show that it's a zip file

# the password is redavni

# OPEN readme.txt:

# Yes! This is really level 21 in here.
# And yes, After you solve it, you'll be in level 22!
#
# Now for the level:
#
# * We used to play this game when we were kids
# * When I had no idea what to do, I looked backwards.
