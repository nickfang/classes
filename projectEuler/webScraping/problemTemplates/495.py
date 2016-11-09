# Writing n as the product of k distinct positive integers

#
#Let W(n,k) be the number of ways in which n can be written as the product of k distinct positive integers.
#For example, W(144,4) = 7. There are 7 ways in which 144 can be written as a product of 4 distinct positive integers:
#<ul><li>144 = 1×2×4×18</li>
#<li>144 = 1×2×8×9</li>
#<li>144 = 1×2×3×24</li>
#<li>144 = 1×2×6×12</li>
#<li>144 = 1×3×4×12</li>
#<li>144 = 1×3×6×8</li>
#<li>144 = 2×3×4×6</li>
#</ul>Note that permutations of the integers themselves are not considered distinct.
#Furthermore, W(100!,10) modulo 1 000 000 007 = 287549200.
#Find W(10000!,30) modulo 1 000 000 007.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))