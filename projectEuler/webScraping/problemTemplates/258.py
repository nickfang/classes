# A lagged Fibonacci sequence

#
#A sequence is defined as:
#
#<ul><li>gk = 1, for 0 ≤ k ≤ 1999</li>
#<li>gk = gk-2000 + gk-1999, for k ≥ 2000.
#</li></ul>Find gk mod 20092010 for k = 10^18.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))