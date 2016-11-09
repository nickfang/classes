# Counting Sundays
#
#You are given the following information, but you may prefer to do some research for yourself.
#  - 1 Jan 1900 was a Monday.
#  - Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#  - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#

import time
import datetime

startTime = time.time()

numSundays = 0

# the datetime module has a function weekday() that returns 6 if the date is a Sunday.  Iterate through the firsts
# of each month and year.  Remember range is for (year = 1901; year < 2001; ++year) {}
for year in range(1901,2001):
	for month in range(1,13):
		date = datetime.date(year,month,1)
		if date.weekday() is 6:
			numSundays += 1

print(numSundays)
print('Elapsed time: ' + str(time.time()-startTime))