# Minimum of subsequences

#
#Let Sn be an integer sequence produced with the following pseudo-random number generator:
#<center><table class="p375"><tr><td style="text-align:right;">S0</td>
#<td>= </td>
#<td>290797 </td>
#</tr><tr><td>Sn+1</td>
#<td>= </td>
#<td>Sn2 mod 50515093</td>
#</tr></table></center>
#
#Let A(i, j) be the minimum of the numbers Si, Si+1, ... , Sj for i ≤ j.
#Let M(N) = ΣA(i, j) for 1 ≤ i ≤ j ≤ N.
#We can verify that M(10) = 432256955 and M(10 000) = 3264567774119.
#
#Find M(2 000 000 000).
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))