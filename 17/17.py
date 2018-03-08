# http://www.pythonchallenge.com/pc/return/romance.html

# cookie
# F12 console alter(document.cookie)
# show you should have followed busynothing


# import urllib2, urllib
# import cookielib
# import re
# import bz2
#
#
# cookie = cookielib.CookieJar()
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# urllib2.install_opener(opener)
#
# p = re.compile("\d+")
# page = "12345"
# secretCode = []
#
#
# for i in range(0, 500):
#     res = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=" + page)
#     secretCode.append(re.findall('info=(.{0,4});', str(res.info())))
#     source = res.read()
#     next = p.findall(source)
#     res.close()
#     if next:
#         print next[-1]
#         page = next[-1]
#     else:
#         break
#
#
#
# code = ''.join([i for m in secretCode for i in m])
# print code
# print bz2.decompress(urllib.unquote_plus(code))



# is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.

# call his father

# xmlprc = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
# print xmlprc.system.listMethods()
# print xmlprc.system.methodHelp('phone')
# print xmlprc.system.methodSignature('phone')
# # print xmlprc.phone('Bert')
# print xmlprc.phone('Leopold')

# http://www.pythonchallenge.com/pc/stuff/violin.php


from urllib2 import Request, urlopen
from urllib import unquote_plus


info = "the flowers are on their way"
url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
req = Request(url, headers={'Cookie': 'info=' + unquote_plus(info)})
print urlopen(req).read()