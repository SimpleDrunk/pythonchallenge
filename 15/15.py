# http://www.pythonchallenge.com/pc/return/uzi.html

import datetime, calendar


year = 1006

for i in range(100):
    year += 10
    if datetime.datetime(year, 1, 26).isoweekday() == 1 and calendar.isleap(year):
        print year


# the second young, so is 1756.1.27, get mozart

