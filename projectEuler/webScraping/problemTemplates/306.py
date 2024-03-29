# Paper-strip Game

#
#The following game is a classic example of Combinatorial Game Theory:
#Two players start with a strip of n white squares and they take alternate turns.
#On each turn, a player picks two contiguous white squares and paints them black.
#The first player who cannot make a move loses.
#<ul><li>If n = 1, there are no valid moves, so the first player loses automatically.</li>
#<li>If n = 2, there is only one valid move, after which the second player loses.</li>
#<li>If n = 3, there are two valid moves, but both leave a situation where the second player loses.</li>
#<li>If n = 4, there are three valid moves for the first player; she can win the game by painting the two middle squares.</li>
#<li>If n = 5, there are four valid moves for the first player (shown below in red); but no matter what she does, the second player (blue) wins.</li>
#</ul><img src="project/images/p306_pstrip.gif" alt="p306_pstrip.gif" />
#So, for 1 ≤ n ≤ 5, there are 3 values of n for which the first player can force a win.
#Similarly, for 1 ≤ n ≤ 50, there are 40 values of n for which the first player can force a win.
#For 1 ≤ n ≤ 1 000 000, how many values of n are there for which the first player can force a win?
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))