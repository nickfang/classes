# Four Representations using Squares

#
#Consider the number 3600. It is very special, because
#
#3600 = 48^2 +     362
#3600 = 20^2 + 2×402
#3600 = 30^2 + 3×302
#3600 = 45^2 + 7×152
#Similarly, we find that 88201 = 99^2 + 2802 = 2872 + 2×542 = 2832 + 3×522 = 1972 + 7×842.
#In 1747, Euler proved which numbers are representable as a sum of two squares.
#We are interested in the numbers n which admit representations of all of the following four types:
#
#n = a12 +   b1^2n = a22 + 2 b22n = a32 + 3 b32n = a72 + 7 b72,
#
#where the ak and bk are positive integers.
#There are 75373 such numbers that do not exceed 107.
#
#How many such numbers are there that do not exceed 2×109?
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))