# Triangle Centres

#
#Consider all the triangles having:
#<ul><li>All their vertices on lattice points (Integer coordinates).</li>
#<li>Circumcentre (Centre of the circumscribed circle) at the origin O.</li>
#<li>Orthocentre (Point where the three altitudes meet) at the point H(5, 0).</li>
#</ul>There are nine such triangles having a perimeter â&permil;¤ 50.
#Listed and shown in ascending order of their perimeter, they are:
#<table><tr><td>A(-4, 3), B(5, 0), C(4, -3)
#A(4, 3), B(5, 0), C(-4, -3)
#A(-3, 4), B(5, 0), C(3, -4)
#A(3, 4), B(5, 0), C(-3, -4)
#A(0, 5), B(5, 0), C(0, -5)
#A(1, 8), B(8, -1), C(-4, -7)
#A(8, 1), B(1, -8), C(-4, 7)
#A(2, 9), B(9, -2), C(-6, -7)
#A(9, 2), B(2, -9), C(-6, 7)</td>
#<td><img src="project/images/p264_TriangleCentres.gif" alt="p264_TriangleCentres.gif" /></td>
#</tr></table>The sum of their perimeters, rounded to four decimal places, is 291.0089.
#Find all such triangles with a perimeter â&permil;¤ 105.
#Enter as your answer the sum of their perimeters rounded to four decimal places.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))