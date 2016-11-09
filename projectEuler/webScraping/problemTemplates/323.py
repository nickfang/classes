# Bitwise-OR operations on random integers

#
#Let y0, y1, y2,... be a sequence of random unsigned 32 bit integers
#(i.e. 0 â&permil;¤ yi &lt; 2^32, every value equally likely).
#For the sequence xi the following recursion is given:<ul><li>x0 = 0 and</li>
#<li>xi = xi-1| yi-1, for i &gt; 0. ( | is the bitwise-OR operator)</li>
#</ul>It can be seen that eventually there will be an index N such that xi = 2^32 -1 (a bit-pattern of all ones) for all i â&permil;Ľ N.
#Find the expected value of N. 
#Give your answer rounded to 10 digits after the decimal point.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))