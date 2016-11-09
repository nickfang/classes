# Selective Amnesia

#
#Larry and Robin play a memory game involving of a sequence of random numbers between 1 and 10, inclusive, that are called out one at a time. Each player can remember up to 5 previous numbers. When the called number is in a player's memory, that player is awarded a point. If it's not, the player adds the called number to his memory, removing another number if his memory is full.
#Both players start with empty memories. Both players always add new missed numbers to their memory but use a different strategy in deciding which number to remove:
#Larry's strategy is to remove the number that hasn't been called in the longest time.
#Robin's strategy is to remove the number that's been in the memory the longest time.
#Example game:<center><table class="p298"><tr><th>Turn</th>
#<th>Callednumber</th>
#<th style="text-align:right;">Larry'smemory</th>
#<th>Larry'sscore</th>
#<th style="text-align:right;">Robin'smemory</th>
#<th>Robin'sscore</th>
#</tr><tr><td>1</td>
#<td>1</td>
#<td style="text-align:right;">1</td>
#<td>0</td>
#<td style="text-align:right;">1</td>
#<td>0</td>
#</tr><tr><td>2</td>
#<td>2</td>
#<td style="text-align:right;">1,2</td>
#<td>0</td>
#<td style="text-align:right;">1,2</td>
#<td>0</td>
#</tr><tr><td>3</td>
#<td>4</td>
#<td style="text-align:right;">1,2,4</td>
#<td>0</td>
#<td style="text-align:right;">1,2,4</td>
#<td>0</td>
#</tr><tr><td>4</td>
#<td>6</td>
#<td style="text-align:right;">1,2,4,6</td>
#<td>0</td>
#<td style="text-align:right;">1,2,4,6</td>
#<td>0</td>
#</tr><tr><td>5</td>
#<td>1</td>
#<td style="text-align:right;">1,2,4,6</td>
#<td>1</td>
#<td style="text-align:right;">1,2,4,6</td>
#<td>1</td>
#</tr><tr><td>6</td>
#<td>8</td>
#<td style="text-align:right;">1,2,4,6,8</td>
#<td>1</td>
#<td style="text-align:right;">1,2,4,6,8</td>
#<td>1</td>
#</tr><tr><td>7</td>
#<td>10</td>
#<td style="text-align:right;">1,4,6,8,10</td>
#<td>1</td>
#<td style="text-align:right;">2,4,6,8,10</td>
#<td>1</td>
#</tr><tr><td>8</td>
#<td>2</td>
#<td style="text-align:right;">1,2,6,8,10</td>
#<td>1</td>
#<td style="text-align:right;">2,4,6,8,10</td>
#<td>2</td>
#</tr><tr><td>9</td>
#<td>4</td>
#<td style="text-align:right;">1,2,4,8,10</td>
#<td>1</td>
#<td style="text-align:right;">2,4,6,8,10</td>
#<td>3</td>
#</tr><tr><td>10</td>
#<td>1</td>
#<td style="text-align:right;">1,2,4,8,10</td>
#<td>2</td>
#<td style="text-align:right;">1,4,6,8,10</td>
#<td>3</td>
#</tr></table></center>
#Denoting Larry's score by L and Robin's score by R, what is the expected value of |L-R| after 50 turns? Give your answer rounded to eight decimal places using the format x.xxxxxxxx .
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))