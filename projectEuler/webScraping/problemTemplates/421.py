# Prime factors of n^15+1

#
#
#Numbers of the form n^15+1 are composite for every integer n &gt; 1.
#For positive integers n and m let s(n,m) be defined as the sum of the distinct prime factors of n^15+1 not exceeding m.
#
#E.g. 2^15+1 = 3×3×11×331.
#So s(2,10) = 3 and s(2,1000) = 3+11+331 = 345.
#
#Also 10^15+1 = 7×11×13×211×241×2161×9091.
#So s(10,100) = 31 and s(10,1000) = 483.
#Find &amp;Sum; s(n,10^8) for 1 ≤ n ≤ 1011.
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))