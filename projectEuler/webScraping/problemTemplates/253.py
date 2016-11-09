# Tidying up

#
#A small child has a “number caterpillar” consisting of forty jigsaw pieces, each with one number on it, which, when connected together in a line, reveal the numbers 1 to 40 in order.
#Every night, the child's father has to pick up the pieces of the caterpillar that have been scattered across the play room. He picks up the pieces at random and places them in the correct order. As the caterpillar is built up in this way, it forms distinct segments that gradually merge together. The number of segments starts at zero (no pieces placed), generally increases up to about eleven or twelve, then tends to drop again before finishing at a single segment (all pieces placed).
#For example:
#
#<table cellspacing="0" cellpadding="2" border="1" align="center"><tr style="background-color:#c1daf9;"><td width="80" align="center">Piece Placed</td>
#<td width="80" align="center">Segments So Far</td></tr><tr><td align="center">12</td><td align="center">1</td></tr><tr><td align="center">4</td><td align="center">2</td></tr><tr><td align="center">29</td><td align="center">3</td></tr><tr><td align="center">6</td><td align="center">4</td></tr><tr><td align="center">34</td><td align="center">5</td></tr><tr><td align="center">5</td><td align="center">4</td></tr><tr><td align="center">35</td><td align="center">4</td></tr><tr><td align="center">…</td><td align="center">…</td></tr></table>
#Let M be the maximum number of segments encountered during a random tidy-up of the caterpillar.
#For a caterpillar of ten pieces, the number of possibilities for each M is
#
#<table cellspacing="0" cellpadding="2" border="1" align="center"><tr style="background-color:#c1daf9;"><td width="50" align="center">M</td>
#<td width="90" align="center">Possibilities</td></tr><tr><td align="center">1</td><td align="right">512      </td></tr><tr><td align="center">2</td><td align="right">250912      </td></tr><tr><td align="center">3</td><td align="right">1815264      </td></tr><tr><td align="center">4</td><td align="right">1418112      </td></tr><tr><td align="center">5</td><td align="right">144000      </td></tr></table>
#so the most likely value of M is 3 and the average value is 385643⁄113400 = 3.400732, rounded to six decimal places.
#The most likely value of M for a forty-piece caterpillar is 11; but what is the average value of M?
#Give your answer rounded to six decimal places.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))