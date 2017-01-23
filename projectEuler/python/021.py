# Amicable numbers

#
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#Evaluate the sum of all the amicable numbers under 10000.
#

import time
import utilsNum

startTime = time.time()

def sumList(list):
	sum = 0
	for x in list:
		sum += x
	return sum

sum = 0
nums = 10000
numsToCheck = [i for i in range(1,nums+1)]
isAmicable = [True for i in range(nums+2)]
for i in numsToCheck:
	if (isAmicable[i] == True):
		pair = sumList(utilsNum.getDivisors(i))
		isAmicable[i] = False
		if (i == sumList(utilsNum.getDivisors(pair)) and (i != pair)):
			isAmicable[pair] = False
			sum += i + pair

print(sum)

print('Elapsed time: ' + str(time.time()-startTime))