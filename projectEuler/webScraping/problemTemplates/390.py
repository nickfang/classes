# Triangles with non rational sides and integral area

#
#Consider the triangle with sides √5, √65 and √68.
#It can be shown that this triangle has area 9.
#S(n) is the sum of the areas of  all triangles with sides √(1+b^2), √(1+c2) and √(b2+c2) (for positive integers b and c ) that have an integral area not exceeding n.
#The example triangle has b=2 and c=8.
#S(106)=18018206.
#Find S(10^10).
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))