# Euler's Number

#
#An infinite sequence of real numbers a(n) is defined for all integers n as follows:
#<img src="project/images/p330_formula.gif" alt="p330_formula.gif" />
#For example,<table class="formula"><tr><td>a(0) = </td>
#<td><table class="frac"><tr><td>1</td></tr><tr><td class="overline">1!</td></tr></table></td>
#<td>+</td>
#<td><table class="frac"><tr><td>1</td></tr><tr><td class="overline">2!</td></tr></table></td>
#<td>+</td>
#<td><table class="frac"><tr><td>1</td></tr><tr><td class="overline">3!</td></tr></table></td>
#<td>+ ... = e − 1 </td>
#</tr></table><table class="formula"><tr><td>a(1) = </td>
#<td><table class="frac"><tr><td>e − 1</td></tr><tr><td class="overline">1!</td></tr></table></td>
#<td>+</td>
#<td><table class="frac"><tr><td>1</td></tr><tr><td class="overline">2!</td></tr></table></td>
#<td>+</td>
#<td><table class="frac"><tr><td>1</td></tr><tr><td class="overline">3!</td></tr></table></td>
#<td>+ ... = 2e − 3 </td>
#</tr></table><table class="formula"><tr><td>a(2) = </td>
#<td><table class="frac"><tr><td>2e − 3</td></tr><tr><td class="overline">1!</td></tr></table></td>
#<td>+</td>
#<td><table class="frac"><tr><td>e − 1</td></tr><tr><td class="overline">2!</td></tr></table></td>
#<td>+</td>
#<td><table class="frac"><tr><td>1</td></tr><tr><td class="overline">3!</td></tr></table></td>
#<td>+ ... =</td>
#<td><table class="frac"><tr><td>7</td></tr><tr><td class="overline">2</td></tr></table></td>
#<td>e − 6 </td>
#</tr></table>
#with e = 2.7182818... being Euler's constant.
#
#
#<table class="formula"><tr><td>It can be shown that a(n) is of the form 
#    </td>
#<td><table class="frac"><tr><td>A(n) e + B(n)</td></tr><tr><td class="overline">n!</td></tr></table></td>
#<td>for integers A(n) and B(n). 
#    </td>
#</tr></table><table class="formula"><tr><td>For example a(10) = 
#    </td>
#<td><table class="frac"><tr><td>328161643 e − 652694486</td></tr><tr><td class="overline">10!</td></tr></table></td>
#<td>.</td>
#</tr></table>
#Find A(10^9) + B(109) and give your answer mod 77 777 777.
#
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))