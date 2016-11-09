# Minkowski Sums

#
#Let Sn be the regular n-sided polygon – or shape – whose vertices 
#
#vk (k = 1,2,…,n) have coordinates:
#<table><tr><td width="40"></td>
#<td>xk   =  
#        cos( 2k-1/n ×180° )</td>
#</tr><tr><td width="40"></td>
#<td>yk   =  
#        sin( 2k-1/n ×180° )</td>
#</tr></table>Each Sn is to be interpreted as a filled shape consisting of all points on the perimeter and in the interior.
#The Minkowski sum, S+T, of two shapes S and T is the result of 
#
#adding every point in S to every point in T, where point addition is performed coordinate-wise: 
#
#(u, v) + (x, y) = (u+x, v+y).
#For example, the sum of S3 and S4 is the six-sided shape shown in pink below:
#
#<img src="project/images/p228.png" alt="picture showing S_3 + S_4" />
#How many sides does S1864 + S1865 + … + S1909 have?
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))