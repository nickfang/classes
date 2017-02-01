# Non-abundant sums

#
#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#

# go through all numbers from 12 to 28123 and store them if they are an abundunt number
# go from 1 to 28123 and start subtracting abundunt numbers if another abundunt number is found move on.  if we reach then abundunt number > current number add the current number to the sum.


import time
import utilsNum

startTime = time.time()

MIN = 12
MAX = 28123
#

def checkAbundantNumber(num):
	sum = 0
	for x in utilsNum.getDivisors(num):
		sum += x
	if sum > num:
		return True
	else:
		return False

def getAbunduntNumbers(num):
	nums = []
	sum = 0
	for x in range(1,num-MIN+1):
		if checkAbundantNumber(x):
			nums.append(x)
	return nums

def removeAbunduntNumbers():
	nums = []
	aNums = getAbunduntNumbers(MAX)
	for x in range(24, MAX+1):
		nums.append(int(x))
	x = 24
	for
	print(nums)

removeAbunduntNumbers()
# print(getAbunduntNumbers(MAX))
# print(checkNumber(12))

print('Elapsed time: ' + str(time.time()-startTime))