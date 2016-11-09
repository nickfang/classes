# Factorial digit sum

#
#n! means n × (n − 1) × ... × 3 × 2 × 1
#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#Find the sum of the digits in the number 100!
#

import time
#from math import factorial

startTime = time.time()

# for some reason this is faster than using the factorial from the math module.
def factorial(num):
	factorial = 1
	for x in range(1,num+1):
		factorial = factorial * x
	return factorial

sum = 0

factorial = factorial(100)
for x in str(factorial):
	sum += int(x)

print(sum)

print('Elapsed time: ' + str(time.time()-startTime))