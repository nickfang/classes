# Sums of power sums

#
#Let fk(n) be the sum of the kth powers of the first n positive integers.
#For example, f2(10) = 1^2 + 22 + 32 + 42 + 52 + 62 + 72 + 82 + 92 + 102 = 385.
#Let Sk(n) be the sum of fk(i) for 1 ≤ i ≤ n. For example, S4(100) = 35375333830.
#What is ∑ (S10000(10^12) mod p) over all primes p between 2 ⋅ 109 and 2 ⋅ 109 + 2000?
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))