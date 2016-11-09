# Dissonant Numbers

#
#Let d(p,n,0) be the multiplicative inverse of n modulo prime p, defined as n × d(p,n,0) = 1 mod p.
#Let d(p,n,k) = $\sum_{i=1}^n$d(p,i,k−1) for k ≥ 1.
#Let D(a,b,k) = $\sum$(d(p,p-1,k) mod p) for all primes a ≤ p &lt; a + b.
#You are given:
#<ul><li>D(101,1,10) = 45</li>
#<li>D(10^3,102,102) = 8334</li>
#<li>D(10^6,103,103) = 38162302</li></ul>Find D(109,105,105).
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))