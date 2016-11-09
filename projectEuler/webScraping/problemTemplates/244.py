# Sliders

#
#You probably know the game Fifteen Puzzle. Here, instead of numbered tiles, we have seven red tiles and eight blue tiles.
#A move is denoted by the uppercase initial of the direction (Left, Right, Up, Down) in which the tile is slid, e.g. starting from configuration (S), by the sequence LULUR we reach the configuration (E):
#
#<table cellspacing="0" cellpadding="2" border="0" align="center"><tr><td width="25">(S)</td><td width="100"><img src="project/images/p244_start.gif" alt="p244_start.gif" /></td><td width="25">, (E)</td><td width="100"><img src="project/images/p244_example.gif" alt="p244_example.gif" /></td>
#</tr></table>
#For each path, its checksum is calculated by (pseudocode):
#
#checksum = 0
#checksum = (checksum × 243 + m1) mod 100 000 007
#checksum = (checksum × 243 + m2) mod 100 000 007
#   …
#checksum = (checksum × 243 + mn) mod 100 000 007
#where mk is the ASCII value of the kth letter in the move sequence and the ASCII values for the moves are:
#
#
#<table cellspacing="0" cellpadding="2" border="1" align="center"><tr><td width="30">L</td><td width="30">76</td></tr><tr><td>R</td><td>82</td></tr><tr><td>U</td><td>85</td></tr><tr><td>D</td><td>68</td></tr></table>
#For the sequence LULUR given above, the checksum would be 19761398.
#Now, starting from configuration (S),
#find all shortest ways to reach configuration (T).
#
#<table cellspacing="0" cellpadding="2" border="0" align="center"><tr><td width="25">(S)</td><td width="100"><img src="project/images/p244_start.gif" alt="p244_start.gif" /></td><td width="25">, (T)</td><td width="100"><img src="project/images/p244_target.gif" alt="p244_target.gif" /></td>
#</tr></table>
#What is the sum of all checksums for the paths having the minimal length?
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))