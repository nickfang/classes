# Polynomials of Fibonacci numbers

#
#The Fibonacci numbers {fn, n ≥ 0} are defined recursively as fn = fn-1 + fn-2 with base cases f0 = 0 and f1 = 1.
#Define the polynomials {Fn, n ≥ 0} as Fn(x) = ∑fixi for 0 ≤ i ≤ n.
#For example, F7(x) = x + x2 + 2x^3 + 3x4 + 5x5 + 8x6 + 13x7, and F7(11) = 268357683.
#Let n = 1015. Find the sum [∑0≤x≤100 Fn(x)] mod 1307674368000 (= 15!).
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))