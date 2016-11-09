# Modulo Summations

#
#
#Let an be a sequence recursively defined by: <img src="project/images/p326_formula1.gif" style="vertical-align:middle;" alt="p326_formula1.gif" />. 
#
#
#So the first 10 elements of an are: 1,1,0,3,0,3,5,4,1,9.
#
#Let f(N,M) represent the number of pairs (p,q) such that: <img src="project/images/p326_formula2.gif" alt="p326_formula2.gif" />
#
#It can be seen that f(10,10)=4 with the pairs (3,3), (5,5), (7,9) and (9,10).
#
#
#You are also given that f(10^4,103)=97158.
#
#Find f(10^12,106).
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))