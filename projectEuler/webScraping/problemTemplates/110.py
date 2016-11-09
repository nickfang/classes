# Diophantine reciprocals II

#
#In the following equation x, y, and n are positive integers.
#
#<table align="center"><tr><td>1x</td>
#<td> + </td>
#<td>1y</td>
#<td> = </td>
#<td>1n</td>
#</tr></table>
#It can be verified that when n = 1260 there are 113 distinct solutions and this is the least value of n for which the total number of distinct solutions exceeds one hundred.
#What is the least value of n for which the number of distinct solutions exceeds four million?
#NOTE: This problem is a much more difficult version of Problem 108 and as it is well beyond the limitations of a brute force approach it requires a clever implementation.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))