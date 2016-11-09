# Reachable Numbers

#
#A positive integer will be called reachable if it can result from an arithmetic expression obeying the following rules:
#<ul><li>Uses the digits 1 through 9, in that order and exactly once each.</li>
#<li>Any successive digits can be concatenated (for example, using the digits 2, 3 and 4 we obtain the number 234).</li>
#<li>Only the four usual binary arithmetic operations (addition, subtraction, multiplication and division) are allowed.</li>
#<li>Each operation can be used any number of times, or not at all.</li>
#<li>Unary minus (A minus sign applied to a single operand (as opposed to a subtraction operator between two operands)) is not allowed.</li>
#<li>Any number of (possibly nested) parentheses may be used to define the order of operations.</li>
#</ul>For example, 42 is reachable, since (1/23) * ((4*5)-6) * (78-9) = 42.
#What is the sum of all positive reachable integers?
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))