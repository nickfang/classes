# Investigating the behaviour of a recursively defined sequence

#
#Given is the function f(x) = ⌊2^30.403243784-x2⌋ × 10-9 ( ⌊ ⌋ is the floor-function),
#the sequence un is defined by u0 = -1 and un+1 = f(un).
#Find un + un+1 for n = 10^12.
#Give your answer with 9 digits after the decimal point.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))