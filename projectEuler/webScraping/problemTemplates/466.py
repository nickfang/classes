# Distinct terms in a multiplication table

#
#Let P(m,n) be the number of distinct terms in an m×n multiplication table.
#For example, a 3×4 multiplication table looks like this:
#<center><table class="p466"><tr><th>×</th> <th>1</th><th>2</th><th>3</th><th>4</th></tr><tr><th>1</th> <td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><th>2</th> <td>2</td><td>4</td><td>6</td><td>8</td></tr><tr><th>3</th> <td>3</td><td>6</td><td>9</td><td>12</td></tr></table></center>
#There are 8 distinct terms {1,2,3,4,6,8,9,12}, therefore P(3,4) = 8.
#You are given that:
#P(64,64) = 1263,
#P(12,345) = 1998, and
#P(32,10^15) = 13826382602124302.
#Find P(64,10^16).
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))