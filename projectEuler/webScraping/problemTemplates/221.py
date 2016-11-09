# Alexandrian Integers

#
#We shall call a positive integer A an "Alexandrian integer", if there exist integers p, q, r such that:
#<table class="formula" style="margin-left:50px;"><tr><td>
#A = p · q · r    and  
#   </td>
#<td>
#<table class="frac"><tr><td>1</td></tr><tr><td class="overline">A</td></tr></table></td>
#<td>=</td>
#<td>
#<table class="frac"><tr><td>1</td></tr><tr><td class="overline">p</td></tr></table></td>
#<td>+</td>
#<td>
#<table class="frac"><tr><td>1</td></tr><tr><td class="overline">q</td></tr></table></td>
#<td>+</td>
#<td>
#<table class="frac"><tr><td>1</td></tr><tr><td class="overline">r</td></tr></table></td>
#</tr></table>For example, 630 is an Alexandrian integer (p = 5, q = −7, r = −18).
#In fact, 630 is the 6th Alexandrian integer,  the first 6 Alexandrian integers being: 6, 42, 120, 156, 420 and 630.
#Find the 150000th Alexandrian integer.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))