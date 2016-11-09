# Crazy Function

#
#
#For fixed integers a, b, c, define the crazy function F(n) as follows:
#F(n) = n - c for all n &gt; b 
#F(n) = F(a + F(a + F(a + F(a + n)))) for all n â&permil;¤ b.
#
#
#Also, define S(a, b, c) = <img src="project/images/p340_formula.gif" style="vertical-align:middle;" alt="p340_formula.gif" />.
#
#
#For example, if a = 50, b = 2000 and c = 40, then F(0) = 3240 and F(2000) = 2040.
#Also, S(50, 2000, 40) = 5204240.
#
#
#Find the last 9 digits of S(21^7, 721, 127).
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))