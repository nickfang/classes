# Sum of digits - experience #23

#
#
#For a positive integer k, define d(k) as the sum of the digits of k in its usual decimal representation.
#Thus d(42) = 4+2 = 6.
#
#
#For a positive integer n, define S(n) as the number of positive integers k &lt; 10n with the following properties :
#<ul><li>k is divisible by 23 and
#</li><li>d(k) = 23.
#</li></ul>
#You are given that S(9) = 263626 and S(42) = 6377168878570056.
#
#
#Find S(11^12) and give your answer mod 109.
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))