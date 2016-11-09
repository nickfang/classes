# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

import time
elapsedTime = time.time()
maxNum = 2000000
primes = [2]
x = 3 
isPrime = True
total = 0
while x < maxNum:
   isPrime = True
   for y in primes:
      if x % y == 0:
         isPrime = False
         break
   if isPrime:
      primes.append(x)
      total += x
      #print x
   x += 2
elapsedTime = time.time() - elapsedTime
print elapsedTime
print total
