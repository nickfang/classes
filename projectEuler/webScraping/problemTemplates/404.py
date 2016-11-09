# Crisscross Ellipses

#
#
#Ea is an ellipse with an equation of the form x^2 + 4y2 = 4a2.
#Ea' is the rotated image of Ea by θ degrees counterclockwise around the origin O(0, 0) for 0° &lt; θ &lt; 90°.
#
#
#<img src="project/images/p404_c_ellipse.gif" alt="p404_c_ellipse.gif" />
#
#b is the distance to the origin of the two intersection points closest to the origin and c is the distance of the two other intersection points.
#We call an ordered triplet (a, b, c) a canonical ellipsoidal triplet if a, b and c are positive integers.
#For example, (209, 247, 286) is a canonical ellipsoidal triplet.
#
#
#Let C(N) be the number of distinct canonical ellipsoidal triplets (a, b, c) for a ≤ N.
#It can be verified that C(10^3) = 7, C(104) = 106 and C(106) = 11845.
#
#
#Find C(10^17).
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))