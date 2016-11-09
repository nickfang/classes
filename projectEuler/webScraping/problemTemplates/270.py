# Cutting Squares

#
#A square piece of paper with integer dimensions N×N is placed with a corner at the origin and two of its sides along the x- and y-axes. Then, we cut it up respecting the following rules:
#<ul><li>We only make straight cuts between two points lying on different sides of the square, and having integer coordinates.</li>
#<li>Two cuts cannot cross, but several cuts can meet at the same border point.</li>
#<li>Proceed until no more legal cuts can be made.</li>
#</ul>Counting any reflections or rotations as distinct, we call C(N) the number of ways to cut an N×N square. For example, C(1) = 2 and C(2) = 30 (shown below).
#<img src="project/images/p270_CutSquare.gif" alt="p270_CutSquare.gif" />
#What is C(30) mod 108 ?
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))