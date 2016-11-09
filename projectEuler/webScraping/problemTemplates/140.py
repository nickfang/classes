# Modified Fibonacci golden nuggets

#
#Consider the infinite polynomial series AG(x) = xG1 + x2G2 + x3G3 + ..., where Gk is the kth term of the second order recurrence relation Gk = Gk−1 + Gk−2, G1 = 1 and G2 = 4; that is, 1, 4, 5, 9, 14, 23, ... .
#For this problem we shall be concerned with values of x for which AG(x) is a positive integer.
#The corresponding values of x for the first five natural numbers are shown below.
#
#<table cellspacing="0" cellpadding="2" border="1" align="center"><tr style="background-color:#c1daf9;"><td>x</td><td width="50">AG(x)</td>
#</tr><tr><td>(√5−1)/4</td><td>1</td>
#</tr><tr><td>2/5</td><td>2</td>
#</tr><tr><td>(√22−2)/6</td><td>3</td>
#</tr><tr><td>(√137−5)/14</td><td>4</td>
#</tr><tr><td>1/2</td><td>5</td>
#</tr></table>
#We shall call AG(x) a golden nugget if x is rational, because they become increasingly rarer; for example, the 20th golden nugget is 211345365.
#Find the sum of the first thirty golden nuggets.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))