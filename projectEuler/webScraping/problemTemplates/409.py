# Nim Extreme

#
#Let n be a positive integer. Consider nim positions where:<ul><li>There are n non-empty piles.
#</li><li>Each pile has size less than 2n.
#</li><li>No two piles have the same size.
#</li></ul>Let W(n) be the number of winning nim positions satisfying the above
#conditions (a position is winning if the first player has a winning strategy). For example, W(1) = 1, W(2) = 6, W(3) = 168, W(5) = 19764360 and W(100) mod 1 000 000 007 = 384777056.
#
#Find W(10 000 000) mod 1 000 000 007.
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))