# A rectangular tiling

#
#
#We wish to tile a rectangle whose length is twice its width.
#Let T(0) be the tiling consisting of a single rectangle.
#For n &gt; 0, let T(n) be obtained from T(n-1) by replacing all tiles in the following manner:
#
#
#<img src="project/images/p405_tile1.png" alt="p405_tile1.png" />
#
#The following animation demonstrates the tilings T(n) for n from 0 to 5:
#
#
#<img src="project/images/p405_tile2.gif" alt="p405_tile2.gif" />
#
#Let f(n) be the number of points where four tiles meet in T(n).
#For example, f(1) = 0, f(4) = 82 and f(10^9) mod 177 = 126897180.
#
#
#Find f(10k) for k = 10^18, give your answer modulo 177.
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))