# Tours on a 4 x n playing board

#
#Let T(n) be the number of tours over a 4 Ă&mdash; n playing board such that:
#<ul><li>The tour starts in the top left corner.</li>
#<li>The tour consists of moves that are up, down, left, or right one square.</li>
#<li>The tour visits each square exactly once.</li>
#<li>The tour ends in the bottom left corner.</li>
#</ul>The diagram shows one tour over a 4 Ă&mdash; 10 board:
#
#<img src="project/images/p237.gif" alt="" />
#T(10) is 2329. What is T(10^12) modulo 108?
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))