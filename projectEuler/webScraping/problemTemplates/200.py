# Find the 200th prime-proof sqube containing the contiguous sub-string "200"

#
#We shall define a sqube to be a number of the form, p^2q3, where p and q are distinct primes.
#For example, 200 = 5^223 or 120072949 = 232613.
#The first five squbes are 72, 108, 200, 392, and 500.
#Interestingly, 200 is also the first number for which you cannot change any single digit to make a prime; we shall call such numbers, prime-proof. The next prime-proof sqube which contains the contiguous sub-string "200" is 1992008.
#Find the 200th prime-proof sqube containing the contiguous sub-string "200".
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))