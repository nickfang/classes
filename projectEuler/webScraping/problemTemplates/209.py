# Circular Logic

#
#A k-input binary truth table is a map from k input bits
#(binary digits, 0 [false] or 1 [true]) to 1 output bit. For example, the 2-input binary truth tables for the logical AND and XOR functions are:
#
#<table cellspacing="0" cellpadding="2" border="1" align="left"><tr style="background-color:#c1daf9;"><td width="30" align="center">x</td>
#<td width="30" align="center">y</td>
#<td>x AND y</td></tr><tr><td align="center">0</td><td align="center">0</td><td align="center">0</td></tr><tr><td align="center">0</td><td align="center">1</td><td align="center">0</td></tr><tr><td align="center">1</td><td align="center">0</td><td align="center">0</td></tr><tr><td align="center">1</td><td align="center">1</td><td align="center">1</td></tr></table><table cellspacing="0" cellpadding="2" border="1" align="right"><tr style="background-color:#c1daf9;"><td width="30" align="center">x</td>
#<td width="30" align="center">y</td>
#<td>x XOR y</td></tr><tr><td align="center">0</td><td align="center">0</td><td align="center">0</td></tr><tr><td align="center">0</td><td align="center">1</td><td align="center">1</td></tr><tr><td align="center">1</td><td align="center">0</td><td align="center">1</td></tr><tr><td align="center">1</td><td align="center">1</td><td align="center">0</td></tr></table>How many 6-input binary truth tables, τ, satisfy the formula
#
#τ(a, b, c, d, e, f) AND τ(b, c, d, e, f, a XOR (b AND c)) = 0
#for all 6-bit inputs (a, b, c, d, e, f)?
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))