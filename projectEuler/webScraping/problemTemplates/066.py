# Diophantine equation

#
#Consider quadratic Diophantine equations of the form:
#x^2 – Dy2 = 1
#For example, when D=13, the minimal solution in x is 649^2 – 13×1802 = 1.
#It can be assumed that there are no solutions in positive integers when D is square.
#By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
#3^2 – 2×22 = 1
#2^2 – 3×12 = 192 – 5×42 = 1
#5^2 – 6×22 = 1
#8^2 – 7×32 = 1
#Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
#Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))