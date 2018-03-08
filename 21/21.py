# f = open(r'./package.pack', 'r')
# res = list(f.read())
# str = ''
# for i in res:
#     hexstr = " %s" % i.encode('hex')
#     str += hexstr
#
# print str

# 78 9c 00 0a 40 f5 bf 78 9c 00 07 40 f8 bf 78 9c 00 06 40 f9 ...
# googling 78 9c, find it's zlib file

import zlib
import bz2
# import binascii


if __name__ == '__main__':
    file = open('./package.pack', 'rb').read()
    data = zlib.decompress(file)
    res = ''
    for i in data:
        hexstr = " %s" % i.encode('hex')
        res += hexstr
    logs= ''
    while True:
        if data[:2] == b'\x78\x9c':
            data = zlib.decompress(data)
            logs += ' '
        elif data[:2] == b'\x42\x5a':
            data = bz2.decompress(data)
            logs += '#'
        elif data[-2:] == b'\x9c\x78':
            data = zlib.decompress(data[::-1])
            logs += '\n'
        else:
            break

    print logs
