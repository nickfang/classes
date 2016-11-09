# Comfortable distance

#
#
#There are N seats in a row. N people come after each other to fill the seats according to the following rules:
#<ol type="1"><li>If there is any seat whose adjacent seat(s) are not occupied take such a seat.</li>
#<li>If there is no such seat and there is any seat for which only one adjacent seat is occupied take such a seat.</li>
#<li>Otherwise take one of the remaining available seats. </li>
#</ol>
#Let T(N) be the number of possibilities that N seats are occupied by N people with the given rules. The following figure shows T(4)=8.
#
#
#
#<img src="project/images/p364_comf_dist.gif" alt="p364_comf_dist.gif" />
#We can verify that T(10) = 61632 and T(1 000) mod 100 000 007 = 47255094.
#Find T(1 000 000) mod 100 000 007.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))