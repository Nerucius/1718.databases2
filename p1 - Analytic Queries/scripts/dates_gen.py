#! /usr/bin/python
import math

years = [2016, 2017]
months = range(0, 12)
weeks = [1,2,3,4]

id = 1

for year in years:

    for month in months:
        quarter = math.ceil( (month+1) / 3.0)
        month_in_quarter = month % 3 +1

        for week in weeks:
            print "%d;%d;%d;%d;%d" % (id, year, quarter, month+1, week)
            id += 1
