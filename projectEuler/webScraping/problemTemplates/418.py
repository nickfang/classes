# Factorisation triples

#
#
#Let n be a positive integer. An integer triple (a, b, c) is called a factorisation triple of n if:<ul><li> 1 ≤ a ≤ b ≤ c
#</li><li> a·b·c = n.
#</li></ul>
#Define f(n) to be a + b + c for the factorisation triple (a, b, c) of n which minimises c / a. One can show that this triple is unique.
#
#
#For example, f(165) = 19, f(100100) = 142 and f(20!) = 4034872.
#
#
#Find f(43!).
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))