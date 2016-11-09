# Exploring Pascal's triangle

#
#We can easily verify that none of the entries in the first seven rows of Pascal's triangle are divisible by 7:
#<table cellpadding="0" cellspacing="0" border="0" align="center"><tr><td> </td>
#<td> </td>
#<td> </td>
#<td> </td>
#<td> </td>
#<td> </td>
#<td> 1</td>
#</tr><tr><td> </td>
#<td> </td>
#<td> </td>
#<td> </td>
#<td> </td>
#<td> 1</td>
#<td> </td>
#<td> 1</td>
#</tr><tr><td> </td>
#<td> </td>
#<td> </td>
#<td> </td>
#<td> 1</td>
#<td> </td>
#<td> 2</td>
#<td> </td>
#<td> 1</td>
#</tr><tr><td> </td>
#<td> </td>
#<td> </td>
#<td> 1</td>
#<td> </td>
#<td> 3</td>
#<td> </td>
#<td> 3</td>
#<td> </td>
#<td> 1</td>
#</tr><tr><td> </td>
#<td> </td>
#<td> 1</td>
#<td> </td>
#<td> 4</td>
#<td> </td>
#<td> 6</td>
#<td> </td>
#<td> 4</td>
#<td> </td>
#<td> 1</td>
#</tr><tr><td> </td>
#<td> 1</td>
#<td> </td>
#<td> 5</td>
#<td> </td>
#<td>10</td>
#<td> </td>
#<td>10</td>
#<td> </td>
#<td> 5</td>
#<td> </td>
#<td> 1</td>
#</tr><tr><td>1</td>
#<td> </td>
#<td> 6</td>
#<td> </td>
#<td>15</td>
#<td> </td>
#<td>20</td>
#<td> </td>
#<td>15</td>
#<td> </td>
#<td> 6</td>
#<td> </td>
#<td> 1</td>
#</tr></table>However, if we check the first one hundred rows, we will find that only 2361 of the 5050 entries are not divisible by 7.
#Find the number of entries which are not divisible by 7 in the first one billion (109) rows of Pascal's triangle.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))