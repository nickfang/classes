# Sum of Squares

#
#Consider equations of the form: a^2 + b2 = N, 0 ≤ a ≤ b, a, b and N integer.
#For N=65 there are two solutions:
#a=1, b=8 and a=4, b=7.
#We call S(N) the sum of the values of a of all solutions of a^2 + b2 = N, 0 ≤ a ≤ b, a, b and N integer.
#Thus S(65) = 1 + 4 = 5.
#Find ∑S(N), for all squarefree N only divisible by primes of the form 4k+1 with 4k+1 &lt; 150.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))