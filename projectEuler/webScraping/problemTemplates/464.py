# Möbius function and intervals

#
#
#The Möbius function, denoted μ(n), is defined as:
#<ul><li>μ(n) = (-1)ω(n) if n is squarefree (where ω(n) is the number of distinct prime factors of n)</li>
#<li>μ(n) = 0 if n is not squarefree.</li>
#</ul>
#Let P(a,b) be the number of integers n in the interval [a,b] such that μ(n) = 1.
#Let N(a,b) be the number of integers n in the interval [a,b] such that μ(n) = -1.
#For example, P(2,10) = 2 and N(2,10) = 4.
#
#
#Let C(n) be the number of integer pairs (a,b) such that:
#<ul><li> 1 ≤ a ≤ b ≤ n,</li>
#<li> 99·N(a,b) ≤ 100·P(a,b), and</li>
#<li> 99·P(a,b) ≤ 100·N(a,b).</li>
#</ul>
#For example, C(10) = 13, C(500) = 16676 and C(10 000) = 20155319.
#
#
#Find C(20 000 000).
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))