# Mountain Range

#
#The following equation represents the continuous topography of a mountainous region, giving the elevation (height above sea level) h at any point (x,y):
#
#<img src="project/images/p262_formula1.gif" alt="p262_formula1.gif" />
#A mosquito intends to fly from A(200,200) to B(1400,1400), without leaving the area given by 0 ≤ x, y ≤ 1600.
#Because of the intervening mountains, it first rises straight up to a point A', having elevation f. Then, while remaining at the same elevation f, it flies around any obstacles until it arrives at a point B' directly above B.
#First, determine fmin which is the minimum constant elevation allowing such a trip from A to B, while remaining in the specified area.
#Then, find the length of the shortest path between A' and B', while flying at that constant elevation fmin.
#Give that length as your answer, rounded to three decimal places.
#Note: For convenience, the elevation function shown above is repeated below, in a form suitable for most programming languages:
#h=( 5000-0.005*(x*x+y*y+x*y)+12.5*(x+y) ) * exp( -abs(0.000001*(x*x+y*y)-0.0015*(x+y)+0.7) )
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))