# Palindrome-containing strings

#
#Let F5(n) be the number of strings s such that:
#<ul><li>s consists only of '0's and '1's,
#</li><li>s has length at most n, and
#</li><li>s contains a palindromic substring of length at least 5.
#</li></ul>For example, F5(4) = 0, F5(5) = 8, 
#F5(6) = 42 and F5(11) = 3844.
#Let D(L) be the number of integers n such that 
#5 ≤ n ≤ L and F5(n) is divisible by 87654321.
#For example, D(10^7) = 0 and D(5·109) = 51.
#Find D(10^18).
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))