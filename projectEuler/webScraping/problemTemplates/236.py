# Luxury Hampers

#
#Suppliers 'A' and 'B' provided the following numbers of products for the luxury hamper market:
#<center><table class="p236"><tr><th>Product</th><th style="text-align:center;">'A'</th><th style="text-align:center;">'B'</th></tr><tr><td>Beluga Caviar</td><td>5248</td><td>640</td></tr><tr><td>Christmas Cake</td><td>1312</td><td>1888</td></tr><tr><td>Gammon Joint</td><td>2624</td><td>3776</td></tr><tr><td>Vintage Port</td><td>5760</td><td>3776</td></tr><tr><td>Champagne Truffles</td><td>3936</td><td>5664</td></tr></table></center>
#Although the suppliers try very hard to ship their goods in perfect condition, there is inevitably some spoilage - i.e. products gone bad.
#The suppliers compare their performance using two types of statistic:<ul><li>The five per-product spoilage rates for each supplier are equal to the number of products gone bad divided by the number of products supplied, for each of the five products in turn.</li>
#<li>The overall spoilage rate for each supplier is equal to the total number of products gone bad divided by the total number of products provided by that supplier.</li></ul>To their surprise, the suppliers found that each of the five per-product spoilage rates was worse (higher) for 'B' than for 'A' by the same factor (ratio of spoilage rates), m&gt;1; and yet, paradoxically, the overall spoilage rate was worse for 'A' than for 'B', also by a factor of m.
#There are thirty-five m&gt;1 for which this surprising result could have occurred, the smallest of which is 1476/1475.
#What's the largest possible value of m?
#Give your answer as a fraction reduced to its lowest terms, in the form u/v.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))