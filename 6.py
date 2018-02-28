import re
import zipfile

p = re.compile("\d+")
page = "90052"

unzipfile = zipfile.ZipFile("d:/channel.zip", "r")
# print unzipfile.infolist()
result = ""


def jump():
    global unzipfile
    global page
    global result
    for i in range(0, 1000):
        f = open("D:/channel/" + page + ".txt", "r")
        source = f.readline()
        next = p.findall(source)
        f.close()
        result += unzipfile.getinfo(page + ".txt").comment
        # result = result.join(str(unzipfile.getinfo(page + ".txt").comment))
        if next:
            page = next[-1]
        else:
            if source.find('Divide by two and keep going.') != -1:
                page = str(int(page)/2)
            else:
                print i, source
                break


jump()
print result