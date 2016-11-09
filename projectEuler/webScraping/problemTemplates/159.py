# Digital root sums of factorisations

#
#A composite number can be factored many different ways.  
#For instance, not including multiplication by one, 24 can be factored in 7 distinct ways:
#
#24 = 2x2x2x3
#24 = 2x3x4
#24 = 2x2x6
#24 = 4x6
#24 = 3x8
#24 = 2x12
#24 = 24
#
#Recall that the digital root of a number, in base 10, is found by adding together the digits of that number, 
#and repeating that process until a number is arrived at that is less than 10.  
#Thus the digital root of 467 is 8.
#We shall call a Digital Root Sum (DRS) the sum of the digital roots of the individual factors of our number.
# The chart below demonstrates all of the DRS values for 24.
#<table align="center" border="1" cellpadding="2" cellspacing="0"><tr><th>Factorisation</th><th>Digital Root Sum</th></tr><tr><td>2x2x2x3</td>
#<td>9</td></tr><tr><td>2x3x4</td>
#<td>9</td></tr><tr><td>2x2x6</td>
#<td>10</td></tr><tr><td>4x6</td>
#<td>10</td></tr><tr><td>3x8</td>
#<td>11</td></tr><tr><td>2x12</td>
#<td>5</td></tr><tr><td>24</td>
#<td>6</td></tr></table>The maximum Digital Root Sum  of 24 is 11.
#The function mdrs(n) gives the maximum Digital Root Sum of n. So  mdrs(24)=11.
#Find â&circ;&lsquo;mdrs(n) for 1 &lt; n &lt; 1,000,000.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))