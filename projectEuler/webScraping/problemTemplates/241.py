# Perfection Quotients

#
#For a positive integer n, let σ(n) be the sum of all divisors of n, so e.g. σ(6) = 1 + 2 + 3 + 6 = 12.
#
#A perfect number, as you probably know, is a number with σ(n) = 2n.
#<table><tr><td>Let us define the perfection quotient of a positive integer as</td><td>p(n)</td><td>= </td>
#<td>σ(n)n</td>
#<td>.</td>
#</tr></table>Find the sum of all positive integers n ≤ 1018 for which p(n) has the form k + 1⁄2, where k is an integer.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))