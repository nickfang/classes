# Sum of sum of divisors

#
#Let d(k) be the sum of all divisors of k.
#We define the function S(N) = ∑1≤i≤N ∑1≤j≤Nd(i·j).
#For example, S(3) = d(1) + d(2) + d(3) + d(2) + d(4) + d(6) + d(3) + d(6) + d(9) = 59.
#You are given that S(10^3) = 563576517282 and S(105) mod 109 = 215766508.
#Find S(10^11) mod 109.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))