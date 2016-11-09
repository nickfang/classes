#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
num = 20
primeNums = range(num+1)[2:num+1:1]
for x in primeNums:
   for y in primeNums:
      if (y % x == 0):
         if y != x:
	    primeNums.remove(y)
print "Prime Number:"
print primeNums

trimmedList = range(num+1)[num+1:1:-1]
for x in trimmedList:
   for y in trimmedList:
      if x % y == 0:
         if x != y:
            trimmedList.remove(y)
print "Trimmed List:"
print trimmedList

def primeFactors(num):
   primes = []
   i = 2
   limit = num**0.5
   while i <= num:
      if num % i == 0:
         primes.append(i)
         num = num / i
      else:
         i += 1
   if num > 1:
      primes.append(num)
   print primes

print "Prime factors of Trimmed List:"
for x in trimmedList:
   temp = primeFactors(x)

# Take the highest power of each prime number from the prime factorization and multiply them together.
