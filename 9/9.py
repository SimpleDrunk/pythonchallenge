import urllib2
import zlib

headers = {
                        "User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6",
          }


try:
    req = urllib2.Request("http://www.pythonchallenge.com/pc/return/good.html", headers = headers)
    res = urllib2.urlopen(req)
    source = res.read()

    start = source.rfind("first:")
    end = source.rfind("second:")
    end2 = source.lfind("-->")
    first = source[start: end - 7]
    second = source[end: end2]

    print first, second

except urllib2.HTTPError as http_error:
    print zlib.decompress(http_error.read(), 30)

#only replace the coord data to the stage 8's page source