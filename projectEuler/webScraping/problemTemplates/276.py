# Primitive Triangles

#
#Consider the triangles with integer sides a, b and c with a â&permil;¤ b â&permil;¤ c.
#An integer sided triangle (a,b,c) is called primitive if  gcd(a,b,c) (gcd(a,b,c)=gcd(a,gcd(b,c)))=1. 
#How many primitive integer sided triangles exist with a perimeter not exceeding 10 000 000?
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))