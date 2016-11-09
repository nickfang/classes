# Fibonacci golden nuggets

#
#Consider the infinite polynomial series AF(x) = xF1 + x2F2 + x3F3 + ..., where Fk is the kth term in the Fibonacci sequence: 1, 1, 2, 3, 5, 8, ... ; that is, Fk = Fk−1 + Fk−2, F1 = 1 and F2 = 1.
#For this problem we shall be interested in values of x for which AF(x) is a positive integer.
#<table cellpadding="0" cellspacing="0" border="0"><tr><td>Surprisingly AF(1/2)</td>
#<td> = </td>
#<td>(1/2).1 + (1/2)^2.1 + (1/2)3.2 + (1/2)4.3 + (1/2)5.5 + ...</td>
#</tr><tr><td> </td>
#<td> = </td>
#<td>1/2 + 1/4 + 2/8 + 3/16 + 5/32 + ...</td>
#</tr><tr><td> </td>
#<td> = </td>
#<td>2</td>
#</tr></table>The corresponding values of x for the first five natural numbers are shown below.
#
#<table cellspacing="0" cellpadding="2" border="1" align="center"><tr style="background-color:#c1daf9;"><td>x</td><td width="50">AF(x)</td>
#</tr><tr><td>√2−1</td><td>1</td>
#</tr><tr><td>1/2</td><td>2</td>
#</tr><tr><td>(√13−2)/3</td><td>3</td>
#</tr><tr><td>(√89−5)/8</td><td>4</td>
#</tr><tr><td>(√34−3)/5</td><td>5</td>
#</tr></table>
#We shall call AF(x) a golden nugget if x is rational, because they become increasingly rarer; for example, the 10th golden nugget is 74049690.
#Find the 15th golden nugget.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))