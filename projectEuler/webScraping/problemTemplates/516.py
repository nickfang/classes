# 5-smooth totients

#
#
#5-smooth numbers are numbers whose largest prime factor doesn't exceed 5.
#5-smooth numbers are also called Hamming numbers.
#Let S(L) be the sum of the numbers n not exceeding L such that Euler's totient function Ď&dagger;(n) is a Hamming number.
#S(100)=3728.
#
#
#Find S(10^12). Give your answer modulo 232.
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))