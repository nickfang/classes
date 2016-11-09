# Largest prime factors of consecutive numbers

#
#Let f(n) be the largest prime factor of n.
#Let g(n) = f(n) + f(n+1) + f(n+2) + f(n+3) + f(n+4) + f(n+5) + f(n+6) + f(n+7) + f(n+8), the sum of the largest prime factor of each of nine consecutive numbers starting with n.
#Let h(n) be the maximum value of g(k) for 2 â&permil;¤ k â&permil;¤ n.
#You are given:
#<ul><li>f(100) = 5</li>
#<li>f(101) = 101</li>
#<li>g(100) = 409</li>
#<li>h(100) = 417</li>
#<li>h(10^9) = 4896292593</li></ul>Find h(1016).
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))