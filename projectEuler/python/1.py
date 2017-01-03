# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import time

numbers = set([])

startTime = time.time()

i = 0
while (i*3<1000):
   numbers.add(i*3)
   i = i + 1
i = 0
while (i*5<1000):
   numbers.add(i*5)
   i = i+1
total = sum(numbers)
print(numbers)
print(total)

print('Elapsed time: ' + str(time.time()-startTime))

startTime = time.time()

numbers = set([])

for x in range(0,1000,3):
	numbers.add(x)
for x in range(0,1000,5):
	# if (x % 3 != 0):
	numbers.add(x)
total = sum(numbers)
print(numbers)
print(total)

print('Elapsed time: ' + str(time.time()-startTime))