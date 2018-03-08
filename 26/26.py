# http://www.pythonchallenge.com/pc/hex/decent.html

# Send a email to leopold.moz@pythonchallenge.com and say sorry


# RECEIVE ↓


# Never mind that.
#
# Have you found my broken zip?
#
# md5: bbb8b499a0eef99b52c7f13f4e78c24b
#
# Can you believe what one mistake can lead to?

# fix the level 24 broken zip


import hashlib

f = open('./mybroken.zip', 'rb').read()
for i in range(len(f)):
    for j in range(256):
        newtext = f[:i]+chr(j)+f[i+1:]
        if hashlib.md5(newtext).hexdigest() == 'bbb8b499a0eef99b52c7f13f4e78c24b':
            open('./new.zip', 'wb').write(newtext)


