# Powers With Trailing Digits

#
#Let f(n) be the largest positive integer x less than 10^9 such that the last 9 digits of nx form the number x (including leading zeros), or zero if no such integer exists.
#For example:
#<ul><li>f(4) = 411728896 (4^411728896 = ...490411728896) </li>
#<li>f(10) = 0</li>
#<li>f(157) = 743757 (157^743757 = ...567000743757)</li>
#<li>Σf(n), 2 ≤ n ≤ 103 = 442530011399</li>
#</ul>Find Σf(n), 2 ≤ n ≤ 106.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))