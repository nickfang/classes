# Convex Holes

#
#
#Given a set of points on a plane, we define a convex hole to be a convex polygon having as vertices any of the given points and not containing any of the given points in its interior (in addition to the vertices, other given points may lie on the perimeter of the polygon). 
#
#
#As an example, the image below shows a set of twenty points and a few such convex holes. 
#The convex hole shown as a red heptagon has an area equal to 1049694.5 square units, which is the highest possible area for a convex hole on the given set of points.
#
#
#<img src="project/images/p252_convexhole.gif" alt="" />
#
#For our example, we used the first 20 points (T2k−1, T2k), for k = 1,2,…,20, produced with the pseudo-random number generator:
#<center><table class="p252"><tr><td style="text-align:right;">S0</td>
#<td>= </td>
#<td>290797 </td>
#</tr><tr><td>Sn+1</td>
#<td>= </td>
#<td>Sn2 mod 50515093</td>
#</tr><tr><td style="text-align:right;">Tn</td>
#<td>= </td>
#<td>( Sn mod 2000 ) − 1000 </td>
#</tr></table></center>
#
#i.e. (527, 144), (−488, 732), (−454, −947), …
#
#
#What is the maximum area for a convex hole on the set containing the first 500 points in the pseudo-random sequence? Specify your answer including one digit after the decimal point.
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))