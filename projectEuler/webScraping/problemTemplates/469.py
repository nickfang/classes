# Empty chairs

#
#
#In a room N chairs are placed around a round table.
#Knights enter the room one by one and choose at random an available empty chair.
#To have enough elbow room the knights always leave at least one empty chair between each other.
#
#
#When there aren't any suitable chairs left, the fraction C of empty chairs is determined.
#We also define E(N) as the expected value of C.
#We can verify that E(4) = 1/2 and E(6) = 5/9.
#
#
#Find E(10^18). Give your answer rounded to fourteen decimal places in the form 0.abcdefghijklmn.
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))