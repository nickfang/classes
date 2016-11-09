# Flipping game

#
#The flipping game is a two player game played on a N by N square board.
#Each square contains a disk with one side white and one side black.
#The game starts with all disks showing their white side.
#A turn consists of flipping all disks in a rectangle with the following properties:
#<ul><li>the upper right corner of the rectangle contains a white disk</li>
#<li>the rectangle width is a perfect square (1, 4, 9, 16, ...)</li>
#<li>the rectangle height is a triangular number (The triangular numbers are defined as Â˝Â n(n + 1) for positive integer n.) (1, 3, 6, 10, ...)</li>
#</ul><img src="project/images/p459-flipping-game-0.png" alt="p459-flipping-game-0.png" />
#Players alternate turns. A player wins by turning the grid all black.
#Let W(N) be the number of winning moves (The first move of a strategy that ensures a win no matter what the opponent plays.) for the first player on a N by N board with all disks white, assuming perfect play.
#W(1) = 1, W(2) = 0, W(5) = 8 and W(102) = 31395.
#For N=5, the first player's eight winning first moves are:
#<img src="project/images/p459-flipping-game-1.png" alt="p459-flipping-game-1.png" />
#<img src="project/images/p459-flipping-game-2.png" alt="p459-flipping-game-2.png" />
#Find W(106).
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))