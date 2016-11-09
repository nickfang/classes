# The inverse summation of coprime couples

#
#
#For an integer M, we define R(M) as the sum of 1/(p·q) for all the integer pairs p and q which satisfy all of these conditions:
#
#<ul><li> 1 ≤ p &lt; q ≤ M</li>
#<li> p + q ≥ M</li>
#<li> p and q are coprime.</li>
#</ul>
#We also define S(N) as the sum of R(i) for 2 ≤ i ≤ N.
#We can verify that S(2) = R(2) = 1/2, S(10) ≈ 6.9147 and S(100) ≈ 58.2962.
#
#
#Find S(107). Give your answer rounded to four decimal places.
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))