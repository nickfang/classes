# Find the largest 0 to 9 pandigital that can be formed by concatenating products

#
#Take the number 6 and multiply it by each of 1273 and 9854:
#6 Ă&mdash; 1273 =  7638
#6 Ă&mdash; 9854 = 59124
#By concatenating these products we get the 1 to 9 pandigital 763859124. We will call 763859124 the "concatenated product of 6 and (1273,9854)". Notice too, that the concatenation of the input numbers, 612739854, is also 1 to 9 pandigital.
#The same can be done for 0 to 9 pandigital numbers.
#What is the largest 0 to 9 pandigital 10-digit concatenated product of an integer with two or more other integers, such that the concatenation of the input numbers is also a 0 to 9 pandigital 10-digit number?
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))