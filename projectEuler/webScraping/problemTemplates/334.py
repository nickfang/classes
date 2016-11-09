# Spilling the beans

#
#In Plato's heaven, there exist an infinite number of bowls in a straight line.
#Each bowl either contains some or none of a finite number of beans.
#A child plays a game, which allows only one kind of move: removing two beans from any bowl, and putting one in each of the two adjacent bowls. The game ends when each bowl contains either one or no beans.
#For example, consider two adjacent bowls containing 2 and 3 beans respectively, all other bowls being empty. The following eight moves will finish the game:
#<img src="project/images/p334_beans.gif" alt="p334_beans.gif" />
#You are given the following sequences:<table class="formula" style="margin-left:50px;"><tr><td>
#t0 = 123456.
#   </td>
#</tr></table><table class="formula" style="margin-left:50px;"><tr><td>
#ti = 
#   </td>
#<td><img src="project/images/p334_cases.gif" alt="p334_cases.gif" /></td>
#<td>
#<table class="formula"><tr><td></td>
#<td>
#<table class="frac"><tr><td>ti-1</td></tr><tr><td class="overline">2</td></tr></table></td>
#<td>
#         ,
#      </td>
#<td></td>
#<td>
#         if ti-1 is even
#      </td>
#</tr><tr><td><img src="project/images/p334_lfloor.gif" alt="p334_lfloor.gif" /></td>
#<td>
#<table class="frac"><tr><td>ti-1</td></tr><tr><td class="overline">2</td></tr></table></td>
#<td>
#<img src="project/images/p334_rfloor.gif" alt="p334_rfloor.gif" /></td>
#<td>
#         926252, 
#      </td>
#<td>
#         if ti-1 is odd
#      </td>
#</tr></table></td><td>
#</td></tr><tr><td></td>
#<td></td>
#<td>
#      where â&OElig;&Scaron;xâ&OElig;&lsaquo; is the floor function
#   </td>
#</tr><tr><td></td>
#<td></td>
#<td>
#      and <img src="project/images/p334_oplus.gif" alt="p334_oplus.gif" /> is the bitwise XOR operator.
#   </td>
#</tr></table><table class="formula" style="margin-left:50px;"><tr><td>
#bi = ( ti mod 2^11) + 1.
#   </td>
#</tr></table>The first two terms of the last sequence are b1 = 289 and b2 = 145.
#If we start with b1 and b2 beans in two adjacent bowls, 3419100 moves would be required to finish the game.
#Consider now 1500 adjacent bowls containing b1, b2,..., b1500 beans respectively, all other bowls being empty. Find how many moves it takes before the game ends.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))