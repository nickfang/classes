# Totient maximum

#
#Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
#
#<table border="1"><tr><td>n</td>
#<td>Relatively Prime</td>
#<td>φ(n)</td>
#<td>n/φ(n)</td>
#</tr><tr><td>2</td>
#<td>1</td>
#<td>1</td>
#<td>2</td>
#</tr><tr><td>3</td>
#<td>1,2</td>
#<td>2</td>
#<td>1.5</td>
#</tr><tr><td>4</td>
#<td>1,3</td>
#<td>2</td>
#<td>2</td>
#</tr><tr><td>5</td>
#<td>1,2,3,4</td>
#<td>4</td>
#<td>1.25</td>
#</tr><tr><td>6</td>
#<td>1,5</td>
#<td>2</td>
#<td>3</td>
#</tr><tr><td>7</td>
#<td>1,2,3,4,5,6</td>
#<td>6</td>
#<td>1.1666...</td>
#</tr><tr><td>8</td>
#<td>1,3,5,7</td>
#<td>4</td>
#<td>2</td>
#</tr><tr><td>9</td>
#<td>1,2,4,5,7,8</td>
#<td>6</td>
#<td>1.5</td>
#</tr><tr><td>10</td>
#<td>1,3,7,9</td>
#<td>4</td>
#<td>2.5</td>
#</tr></table>
#It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
#Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))