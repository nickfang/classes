# Pivotal Square Sums

#
#Let us call a positive integer k a square-pivot, if there is a pair of integers m &gt; 0 and n â&permil;Ľ k, such that the sum of the (m+1) consecutive squares up to k equals the sum of the m consecutive squares from (n+1) on:
#
#(k-m)^2 + ... + k2 = (n+1)2 + ... + (n+m)2.
#Some small square-pivots are
#<ul><li>4: 3^2 + 42
# = 52</li>
#<li>21: 20^2 + 212 = 292</li>
#<li>24: 21^2 + 222 + 232 + 242 = 252 + 262 + 272</li>
#<li>110: 108^2 + 1092 + 1102 = 1332 + 1342</li></ul>Find the sum of all distinct square-pivots â&permil;¤ 1010.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))