#The following iterative sequence is defined for the set of positive integers:

#n > n/2 (n is even)
#n > 3n + 1 (n is odd)

#Using the rule above and starting with 13, we generate the following sequence:

#13 > 40 > 20 > 10 > 5 > 16 > 8 > 4 > 2 > 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
#Although it has not bproved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

#Which starting number, under one million, produces the longest chain?

#NOTE: Once the chain starts the terms are allowed to go above one million.
#runtime: 5.09026384354

import time

startTime = time.time()
def processNum(num):
   if num&0b1:
      return 3 * num + 1
   else:
      return num >> 2

chainMap = [0]
maxTerms = 0
for x in range (1,1000000):
   num = x
   count = 1
   while num > 1: 
      num = processNum(num)
      if num < x:
         count += chainMap[num]
         break
      else:
         count += 1
   chainMap.append(count)
   if (count > maxTerms):
      maxTerms = count
      startNumber = x
print(time.time() - startTime)
print(startNumber, maxTerms)
