# Prime triples and geometric sequences

#
#Let S(n) = a+b+c over all triples (a,b,c) such that:
#<ul style="list-style-type:disc;"><li>a, b, and c are prime numbers.</li>
#<li>a &lt; b &lt; c &lt; n.</li>
#<li>a+1, b+1, and c+1 form a geometric sequence.</li>
#</ul>For example, S(100) = 1035 with the following triples: 
#(2, 5, 11), (2, 11, 47), (5, 11, 23), (5, 17, 53), (7, 11, 17), (7, 23, 71), (11, 23, 47), (17, 23, 31), (17, 41, 97), (31, 47, 71), (71, 83, 97)
#Find S(108).
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))