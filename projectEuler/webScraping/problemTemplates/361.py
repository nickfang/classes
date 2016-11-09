# Subsequence of Thue-Morse sequence

#
#The Thue-Morse sequence {Tn} is a binary sequence satisfying:
#<ul><li>T0 = 0</li>
#<li>T2n = Tn</li>
#<li>T2n+1 = 1 - Tn</li>
#</ul>
#The first several terms of {Tn} are given as follows:
#01101001100101101001011001101001....
#
#
#We define {An} as the sorted sequence of integers such that the binary expression of each element appears as a subsequence in {Tn}.
#For example, the decimal number 18 is expressed as 10010 in binary. 10010 appears in {Tn} (T8 to T12), so 18 is an element of {An}.
#The decimal number 14 is expressed as 1110 in binary. 1110 never appears in {Tn}, so 14 is not an element of {An}.
#
#
#The first several terms of An are given as follows:
#<table cellspacing="1" cellpadding="5" border="0" align="center"><tr><td align="left">n</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>â&euro;Ś</td></tr><tr><td>An</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>18</td><td>â&euro;Ś</td></tr></table>
#
#We can also verify that A100 = 3251 and A1000 = 80852364498.
#
#
#Find the last 9 digits of <img style="vertical-align:middle;" src="project/images/p361_Thue-Morse1.gif" alt="p361_Thue-Morse1.gif" />.
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))