# Reflexive Position

#
#
#Let's call S the (infinite) string that is made by concatenating the consecutive positive integers (starting from 1)  written down in base 10. 
#Thus, S = 1234567891011121314151617181920212223242...
#
#
#It's easy to see that any number will show up an infinite number of times in S.
#
#
#Let's call f(n) the starting position of the nth occurrence of n in S. 
#For example, f(1)=1, f(5)=81, f(12)=271 and f(7780)=111111365.
#
#
#Find ∑f(3k) for 1≤k≤13.
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))