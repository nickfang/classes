# Infinite string tour

#
#Create a sequence of numbers using the "Blum Blum Shub" pseudo-random number generator:
#<center><table class="p238"><tr><td style="text-align:right;">s0</td>
#<td>=</td>
#<td>14025256</td>
#</tr><tr><td>sn+1</td>
#<td>=</td>
#<td>sn2 mod 20300713</td>
#</tr></table></center>
#Concatenate these numbers  s0s1s2… to create a string w of infinite length.
#Then, w = 14025256741014958470038053646…
#For a positive integer k, if no substring of w exists with a sum of digits equal to k, p(k) is defined to be zero. If at least one substring of w exists with a sum of digits equal to k, we define p(k) = z, where z is the starting position of the earliest such substring.
#For instance:
#The substrings 1, 14, 1402, … 
#with respective sums of digits equal to 1, 5, 7, …
#start at position 1, hence p(1) = p(5) = p(7) = … = 1.
#The substrings 4, 402, 4025, …
#with respective sums of digits equal to 4, 6, 11, …
#start at position 2, hence p(4) = p(6) = p(11) = … = 2.
#The substrings 02, 0252, …
#with respective sums of digits equal to 2, 9, …
#start at position 3, hence p(2) = p(9) = … = 3.
#Note that substring 025 starting at position 3, has a sum of digits equal to 7, but there was an earlier substring (starting at position 1) with a sum of digits equal to 7, so p(7) = 1, not 3.
#We can verify that, for 0 &lt; k ≤ 103, ∑ p(k) = 4742.
#Find ∑ p(k), for 0 &lt; k ≤ 2·10^15.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))