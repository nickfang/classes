# The totient of a square is a cube

#
#
#Consider the number 50.
#50^2 = 2500 = 22 × 54, so φ(2500) = 2 × 4 × 53 = 8 × 53 = 23 × 53. 1
#So 2500 is a square and  φ(2500) is a cube.
#
#
#Find the sum of all numbers n, 1 &amp;lt n &lt; 10^10 such that φ(n2) is a cube.
#
#
#1 φ denotes Euler's totient function.
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))