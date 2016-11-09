# Coresilience

#
#We shall call a fraction that cannot be cancelled down a resilient fraction. Furthermore we shall define the resilience of a denominator, R(d), to be the ratio of its proper fractions that are resilient; for example, R(12) = 4⁄11.
#<table><tr><td>The resilience of a number d &gt; 1 is then</td>
#<td>φ(d)d − 1</td>
#<td>, where φ is Euler's totient function.</td>
#</tr></table><table><tr><td>We further define the coresilience of a number n &gt; 1 as C(n)</td><td>= </td>
#<td>n − φ(n)n − 1</td><td>.</td>
#</tr></table><table><tr><td>The coresilience of a prime p is C(p)</td>
#<td>= </td>
#<td>1p − 1</td><td>.</td>
#</tr></table>Find the sum of all composite integers 1 &lt; n ≤ 2×10^11, for which C(n) is a unit fraction (A fraction with numerator 1).
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))