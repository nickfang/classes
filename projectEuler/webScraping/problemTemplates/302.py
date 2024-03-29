# Strong Achilles Numbers

#
#
#A positive integer n is powerful if p2 is a divisor of n for every prime factor p in n.
#
#
#A positive integer n is a perfect power if n can be expressed as a power of another positive integer.
#
#
#A positive integer n is an Achilles number if n is powerful but not a perfect power. For example, 864 and 1800 are Achilles numbers: 864 = 2^5·33 and 1800 = 23·32·52.
#
#
#We shall call a positive integer S a Strong Achilles number if both S and φ(S) are Achilles numbers.1
#For example, 864 is a Strong Achilles number: φ(864) = 288 = 2^5·32. However, 1800 isn't a Strong Achilles number because: φ(1800) = 480 = 25·31·51.
#
#There are 7 Strong Achilles numbers below 10^4 and 656 below 108.
#
#
#How many Strong Achilles numbers are there below 10^18?
#
#
#1 φ denotes Euler's totient function.
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))