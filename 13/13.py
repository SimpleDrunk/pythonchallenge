# http://www.pythonchallenge.com/pc/return/evil.html


import xmlrpclib


xmlprc = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print xmlprc.system.listMethods()
print xmlprc.system.methodHelp('phone')
print xmlprc.system.methodSignature('phone')
# print xmlprc.phone('Bert')
print xmlprc.phone('Leopold')