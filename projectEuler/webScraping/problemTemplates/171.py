# Finding numbers for which the sum of the squares of the digits is a square

#
#For a positive integer n, let f(n) be the sum of the squares of the digits (in base 10) of n, e.g.
#f(3) = 32 = 9,
#f(25) = 2^2 + 52 = 4 + 25 = 29,
#f(442) = 4^2 + 42 + 22 = 16 + 16 + 4 = 36
#Find the last nine digits of the sum of all n, 0 &lt; n &lt; 10^20, such that f(n) is a perfect square.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))