# Polynomials with at least one integer root

#
#A root or zero of a polynomial P(x) is a solution to the equation P(x) = 0. 
#Define Pn as the polynomial whose coefficients are the digits of n.
#For example, P5703(x) = 5x^3 + 7x2 + 3.
#We can see that:<ul><li>Pn(0) is the last digit of n,</li>
#<li>Pn(1) is the sum of the digits of n,</li>
#<li>Pn(10) is n itself.</li></ul>Define Z(k) as the number of positive integers, n, not exceeding k for which the polynomial Pn has at least one integer root.
#It can be verified that Z(100 000) is 14696.
#What is Z(10^16)?
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))