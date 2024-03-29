# Biclinic Integral Quadrilaterals

#
#ABCD is a convex, integer sided quadrilateral with 1 ≤ AB &lt; BC &lt; CD &lt; AD.
#BD has integer length. O is the midpoint of BD. AO has integer length.
#We'll call ABCD a biclinic integral quadrilateral if AO = CO ≤ BO = DO.
#For example, the following quadrilateral is a biclinic integral quadrilateral:
#AB = 19, BC = 29, CD = 37, AD = 43, BD = 48 and AO = CO = 23.
#
#<img src="project/images/p311_biclinic.gif" alt="p311_biclinic.gif" />
#Let B(N) be the number of distinct biclinic integral quadrilaterals ABCD that satisfy AB^2+BC2+CD2+AD2 ≤ N.
#We can verify that B(10 000) = 49 and B(1 000 000) = 38239.
#
#Find B(10 000 000 000).
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))