# Coin partitions

#
#Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.
#
#<table cellspacing="0" cellpadding="10"><tr><td>OOOOO</td>
#</tr><tr><td>OOOO   O</td>
#</tr><tr><td>OOO   OO</td>
#</tr><tr><td>OOO   O   O</td>
#</tr><tr><td>OO   OO   O</td>
#</tr><tr><td>OO   O   O   O</td>
#</tr><tr><td>O   O   O   O   O</td>
#</tr></table>
#Find the least value of n for which p(n) is divisible by one million.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))