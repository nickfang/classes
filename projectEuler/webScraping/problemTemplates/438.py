# Integer part of polynomial equation's solutions

#
#
#For an n-tuple of integers t = (a1, ..., an), let (x1, ..., xn) be the solutions of the polynomial equation xn + a1xn-1 + a2xn-2 + ... + an-1x + an = 0.
#
#
#Consider the following two conditions:
#<ul><li>x1, ..., xn are all real.
#</li><li>If x1, ..., xn are sorted, ⌊xi⌋ = i for 1 ≤ i ≤ n. (⌊·⌋: floor function.)
#</li></ul>
#In the case of n = 4, there are 12 n-tuples of integers which satisfy both conditions.
#We define S(t) as the sum of the absolute values of the integers in t.
#For n = 4 we can verify that ∑S(t) = 2087 for all n-tuples t which satisfy both conditions.
#
#
#Find ∑S(t) for n = 7.
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))