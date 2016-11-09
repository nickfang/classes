# Pencils of rays

#
#
#Let R(M, N) be the number of lattice points (x, y) which satisfy M&lt;x≤N, M&lt;y≤N and <img style="vertical-align:middle;" src="project/images/p372_pencilray1.jpg" alt="p372_pencilray1.jpg" /> is odd.
#We can verify that R(0, 100) = 3019 and R(100, 10000) = 29750422.
#Find R(2·10^6, 109).
#
#
#Note: <img style="vertical-align:middle;" src="project/images/p372_pencilray2.gif" alt="p372_pencilray2.gif" /> represents the floor function.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))