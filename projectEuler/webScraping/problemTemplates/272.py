# Modular Cubes, part 2

#
#
#For a positive number n, define C(n) as the number of the integers x, for which 1&lt;x&lt;n andx3â&permil;Ą1 mod n.
#
#
#When n=91, there are 8 possible values for x, namely : 9, 16, 22, 29, 53, 74, 79, 81.
#Thus, C(91)=8.
#
#Find the sum of the positive numbers nâ&permil;¤10^11 for which C(n)=242.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))