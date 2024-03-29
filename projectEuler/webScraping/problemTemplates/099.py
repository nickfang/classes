# Largest exponential

#
#Comparing two numbers written in index form like 2^11 and 37 is not difficult, as any calculator would confirm that 211 = 2048 &lt; 37 = 2187.
#However, confirming that 632382^518061 &gt; 519432525806 would be much more difficult, as both numbers contain over three million digits.
#Using <a href="project/resources/p099_base_exp.txt">base_exp.txt</a> (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.
#NOTE: The first two lines in the file represent the numbers in the example given above.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))