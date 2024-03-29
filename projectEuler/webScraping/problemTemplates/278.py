# Linear Combinations of Semiprimes

#
#
#Given the values of integers 1 &lt; a1 &lt; a2 &lt;... &lt; an, consider the linear combinationq1a1 + q2a2 + ... + qnan = b, using only integer values qk ≥ 0. 
#
#
#Note that for a given set of ak, it may be that not all values of b are possible.
#For instance, if a1 = 5 and a2 = 7, there are no q1 ≥ 0 and q2 ≥ 0 such that b could be 
#1, 2, 3, 4, 6, 8, 9, 11, 13, 16, 18 or 23.
#
#In fact, 23 is the largest impossible value of b for a1 = 5 and a2 = 7. We therefore call f(5, 7) = 23. Similarly, it can be shown that f(6, 10, 15)=29 and f(14, 22, 77) = 195.
#
#
#Find ∑ f(p*q,p*r,q*r), where p, q and r are prime numbers and p &amp;lt q &lt; r &lt; 5000.
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))