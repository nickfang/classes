# Reciprocal cycles II

#
#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#<blockquote>
#<table><tr><td>1/2</td><td>= </td><td>0.5</td>
#</tr><tr><td>1/3</td><td>= </td><td>0.(3)</td>
#</tr><tr><td>1/4</td><td>= </td><td>0.25</td>
#</tr><tr><td>1/5</td><td>= </td><td>0.2</td>
#</tr><tr><td>1/6</td><td>= </td><td>0.1(6)</td>
#</tr><tr><td>1/7</td><td>= </td><td>0.(142857)</td>
#</tr><tr><td>1/8</td><td>= </td><td>0.125</td>
#</tr><tr><td>1/9</td><td>= </td><td>0.(1)</td>
#</tr><tr><td>1/10</td><td>= </td><td>0.1</td>
#</tr></table></blockquote>
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
#Unit fractions whose denominator has no other prime factors than 2 and/or 5 are not considered to have a recurring cycle.
#We define the length of the recurring cycle of those unit fractions as 0. 
#
#
#Let L(n) denote the length of the recurring cycle of 1/n.
#You are given that ∑L(n) for 3 ≤ n ≤ 1 000 000 equals 55535191115.
#
#
#Find ∑L(n) for 3 ≤ n ≤ 100 000 000
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))