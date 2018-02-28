import re
import urllib2

p = re.compile("\d+")
page = "90052"


def jump():
    global page
    for i in range(0, 500):
        res = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + page)
        source = res.read()
        next = p.findall(source)
        res.close()
        if next:
            print next[-1]
            page = next[-1]
        else:
            if source.find('Divide by two and keep going.') != -1:
                page = str(int(page)/2)
            else:
                print i, source
                break


jump()