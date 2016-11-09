# Investigating in how many ways objects of two different colours can be grouped

#
#Having three black objects B and one white object W they can be grouped in 7 ways like this:
#<table cellpadding="10" align="center"><tr><td>(BBBW)</td><td>(B,BBW)</td><td>(B,B,BW)</td><td>(B,B,B,W)</td>
#<td>(B,BB,W)</td><td>(BBB,W)</td><td>(BB,BW)</td>
#</tr></table>In how many ways can sixty black objects B and forty white objects W be  thus grouped?
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))