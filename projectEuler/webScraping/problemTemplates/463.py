# A weird recurrence relation

#
#
#The function $f$ is defined for all positive integers as follows:
#<ul><li>$f(1)=1$
#</li><li>$f(3)=3$
#</li><li>$f(2n)=f(n)$
#</li><li>$f(4n + 1)=2f(2n + 1) - f(n)$
#</li><li>$f(4n + 3)=3f(2n + 1) - 2f(n)$
#</li>
#</ul>The function $S(n)$ is defined as $\sum_{i=1}^{n}f(i)$.
#$S(8)=22$ and $S(100)=3604$.
#Find $S(3^{37})$. Give the last 9 digits of your answer.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))