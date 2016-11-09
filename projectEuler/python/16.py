#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 21000?

#Solution:
#1366
#Elapsed time: -0.00122904777527

import time

startTime = time.time()

def getTwoToPower(power):
   return 1 << power         # bit shift to the right to do 2^power

def sumDigits(numString):
   total = 0
   for x in numString[:]:    # iterate over all the characters in the string
      total += int(x)
   return total

print sumDigits(str(getTwoToPower(1000)))
print("Elapsed time: " + str(startTime - time.time()))
