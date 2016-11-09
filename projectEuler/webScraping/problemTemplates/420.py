# 2x2 positive integer matrix

#
#A positive integer matrix is a matrix whose elements are all positive integers.
#Some positive integer matrices can be expressed as a square of a positive integer matrix in two different ways. Here is an example:
#
#<img src="project/images/p420_matrix.gif" alt="p420_matrix.gif" />
#
#We define F(N) as the number of the 2x2 positive integer matrices which have a trace (the sum of the elements on the main diagonal) less than N and which can be expressed as a square of a positive integer matrix in two different ways.
#We can verify that F(50) = 7 and F(1000) = 1019.
#
#
#Find F(107).
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))