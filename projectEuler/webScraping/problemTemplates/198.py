# Ambiguous Numbers

#
#A best approximation to a real number x for the denominator bound d is a rational number r/s (in reduced form) with s â&permil;¤ d, so that any rational number p/q which is closer to x than r/s has q &gt; d.
#Usually the best approximation to a real number is uniquely determined for all denominator bounds. However, there are some exceptions, e.g. 9/40 has the two best approximations 1/4 and 1/5 for the denominator bound 6.
#We shall call a real number x ambiguous, if there is at least one denominator bound for which x possesses two best approximations. Clearly, an ambiguous number is necessarily rational.
#How many ambiguous numbers x = p/q,
#0 &lt; x &lt; 1/100, are there whose denominator q does not exceed 108?
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))