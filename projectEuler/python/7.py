#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
numPrimes = 10001
primes = []
x = 2 
num = 0
isPrime = True
while num < numPrimes:
   isPrime = True
   for y in primes:
      if x % y == 0:
         isPrime = False
         break
   if isPrime:
      primes.append(x)
      num += 1
      print x
   x += 1
print primes
