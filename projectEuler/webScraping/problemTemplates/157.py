# Solving the diophantine equation 1/a+^1/b= p/10n

#
#Consider the diophantine equation 1/a+^1/b= p/10n with a, b, p, n positive integers and a ≤ b.
#For n=1 this equation has 20 solutions that are listed below:
#<table><tr><td width="120">1/1+1/1=20/10</td>
#<td width="120">1/1+1/2=15/10</td>
#<td width="120">1/1+1/5=12/10</td>
#<td width="120">1/1+1/10=11/10</td>
#<td width="120">1/2+1/2=10/10</td>
#</tr><tr><td width="120">1/2+1/5=7/10</td>
#<td width="120">1/2+1/10=6/10</td>
#<td width="120">1/3+1/6=5/10</td>
#<td width="120">1/3+1/15=4/10</td>
#<td width="120">1/4+1/4=5/10</td>
#</tr><tr><td width="120">1/4+1/20=3/10</td>
#<td width="120">1/5+1/5=4/10</td>
#<td width="120">1/5+1/10=3/10</td>
#<td width="120">1/6+1/30=2/10</td>
#<td width="120">1/10+1/10=2/10</td>
#</tr><tr><td width="120">1/11+1/110=1/10</td>
#<td width="120">1/12+1/60=1/10</td>
#<td width="120">1/14+1/35=1/10</td>
#<td width="120">1/15+1/30=1/10</td>
#<td width="120">1/20+1/20=1/10</td>
#</tr></table>How many solutions has this equation for 1 ≤ n ≤ 9?
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))