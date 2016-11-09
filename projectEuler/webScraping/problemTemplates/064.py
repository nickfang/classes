# Odd period square roots

#
#All square roots are periodic when written as continued fractions and can be written in the form:
#
#<table border="0" cellspacing="0" cellpadding="0"><tr><td>√N = a0 +</td>
#<td colspan="3" style="border-bottom:1px solid #000;">1</td>
#</tr><tr><td> </td>
#<td>a1 +</td>
#<td colspan="2" style="border-bottom:1px solid #000;">1</td>
#</tr><tr><td> </td>
#<td> </td>
#<td>a2 +</td>
#<td style="border-bottom:1px solid #000;">1</td>
#</tr><tr><td> </td>
#<td> </td>
#<td> </td>
#<td>a3 + ...</td>
#</tr></table>
#For example, let us consider √23:
#
#<table border="0" cellspacing="0" cellpadding="0"><tr><td>√23 = 4 + √23 — 4 = 4 + </td>
#<td style="border-bottom:1px solid #000;">1</td>
#<td> = 4 + </td>
#<td colspan="2" style="border-bottom:1px solid #000;">1</td>
#</tr><tr><td> </td>
#<td>1√23—4</td>
#<td> </td>
#<td>1 + </td>
#<td>√23 – 37</td>
#</tr></table>
#If we continue we would get the following expansion:
#
#<table border="0" cellspacing="0" cellpadding="0"><tr><td>√23 = 4 +</td>
#<td colspan="4" style="border-bottom:1px solid #000;">1</td>
#</tr><tr><td> </td>
#<td>1 +</td>
#<td colspan="3" style="border-bottom:1px solid #000;">1</td>
#</tr><tr><td> </td>
#<td> </td>
#<td>3 +</td>
#<td colspan="2" style="border-bottom:1px solid #000;">1</td>
#</tr><tr><td> </td>
#<td> </td>
#<td> </td>
#<td>1 +</td>
#<td style="border-bottom:1px solid #000;">1</td>
#</tr><tr><td> </td>
#<td> </td>
#<td> </td>
#<td> </td>
#<td>8 + ...</td>
#</tr></table>
#The process can be summarised as follows:
#
#<table border="0" cellspacing="0" cellpadding="0"><tr><td>a0 = 4,</td>
#<td> </td>
#<td>1√23—4</td>
#<td> = </td>
#<td>√23+47</td>
#<td> = 1 + </td>
#<td>√23—37</td>
#</tr><tr><td>a1 = 1,</td>
#<td> </td>
#<td>7√23—3</td>
#<td> = </td>
#<td>7(√23+3)14</td>
#<td> = 3 + </td>
#<td>√23—32</td>
#</tr><tr><td>a2 = 3,</td>
#<td> </td>
#<td>2√23—3</td>
#<td> = </td>
#<td>2(√23+3)14</td>
#<td> = 1 + </td>
#<td>√23—47</td>
#</tr><tr><td>a3 = 1,</td>
#<td> </td>
#<td>7√23—4</td>
#<td> = </td>
#<td>7(√23+4)7</td>
#<td> = 8 + </td>
#<td>√23—4</td>
#</tr><tr><td>a4 = 8,</td>
#<td> </td>
#<td>1√23—4</td>
#<td> = </td>
#<td>√23+47</td>
#<td> = 1 + </td>
#<td>√23—37</td>
#</tr><tr><td>a5 = 1,</td>
#<td> </td>
#<td>7√23—3</td>
#<td> = </td>
#<td>7(√23+3)14</td>
#<td> = 3 + </td>
#<td>√23—32</td>
#</tr><tr><td>a6 = 3,</td>
#<td> </td>
#<td>2√23—3</td>
#<td> = </td>
#<td>2(√23+3)14</td>
#<td> = 1 + </td>
#<td>√23—47</td>
#</tr><tr><td>a7 = 1,</td>
#<td> </td>
#<td>7√23—4</td>
#<td> = </td>
#<td>7(√23+4)7</td>
#<td> = 8 + </td>
#<td>√23—4</td>
#</tr></table>
#It can be seen that the sequence is repeating. For conciseness, we use the notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.
#The first ten continued fraction representations of (irrational) square roots are:
#√2=[1;(2)], period=1
#√3=[1;(1,2)], period=2
#√5=[2;(4)], period=1
#√6=[2;(2,4)], period=2
#√7=[2;(1,1,1,4)], period=4
#√8=[2;(1,4)], period=2
#√10=[3;(6)], period=1
#√11=[3;(3,6)], period=2
#√12= [3;(2,6)], period=2
#√13=[3;(1,1,1,1,6)], period=5
#Exactly four continued fractions, for N ≤ 13, have an odd period.
#How many continued fractions for N ≤ 10000 have an odd period?
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))