# Triangle Triples

#
#
#<table class="formula"><tr><td>
#Let T(n) be the nth triangle number, so T(n) =
#</td>
#<td>
#<table class="frac" style="font-size:smaller;"><tr><td>n (n+1)</td></tr><tr><td class="overline">2</td></tr></table></td>
#<td>
#.
#</td>
#</tr></table>
#Let dT(n) be the number of divisors of T(n).
#E.g.:
#T(7) = 28 and dT(7) = 6.
#
#
#Let Tr(n) be the number of triples (i, j, k) such that 1 ≤ i &lt; j &lt; k ≤ n and dT(i) &gt; dT(j) &gt; dT(k).
#Tr(20) = 14, Tr(100) = 5772 and Tr(1000) = 11174776.
#
#
#Find Tr(60 000 000). 
#Give the last 18 digits of your answer.
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))