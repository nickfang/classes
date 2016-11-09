# An amazing Prime-generating Automaton

#
#A program written in the programming language Fractran consists of a list of fractions.
#The internal state of the Fractran Virtual Machine is a positive integer, which is initially set to a seed value. Each iteration of a Fractran program multiplies the state integer by the first fraction in the list which will leave it an integer.
#For example, one of the Fractran programs that John Horton Conway wrote for prime-generation consists of the following 14 fractions:<table class="formula"><tr><td><table class="frac"><tr><td>17</td></tr><tr><td class="overline">91</td></tr></table></td>
#<td>,</td>
#<td><table class="frac"><tr><td>78</td></tr><tr><td class="overline">85</td></tr></table></td>
#<td>,</td>
#<td><table class="frac"><tr><td>19</td></tr><tr><td class="overline">51</td></tr></table></td>
#<td>,</td>
#<td><table class="frac"><tr><td>23</td></tr><tr><td class="overline">38</td></tr></table></td>
#<td>,</td>
#<td><table class="frac"><tr><td>29</td></tr><tr><td class="overline">33</td></tr></table></td>
#<td>,</td>
#<td><table class="frac"><tr><td>77</td></tr><tr><td class="overline">29</td></tr></table></td>
#<td>,</td>
#<td><table class="frac"><tr><td>95</td></tr><tr><td class="overline">23</td></tr></table></td>
#<td>,</td>
#<td><table class="frac"><tr><td>77</td></tr><tr><td class="overline">19</td></tr></table></td>
#<td>,</td>
#<td><table class="frac"><tr><td>1</td></tr><tr><td class="overline">17</td></tr></table></td>
#<td>,</td>
#<td><table class="frac"><tr><td>11</td></tr><tr><td class="overline">13</td></tr></table></td>
#<td>,</td>
#<td><table class="frac"><tr><td>13</td></tr><tr><td class="overline">11</td></tr></table></td>
#<td>,</td>
#<td><table class="frac"><tr><td>15</td></tr><tr><td class="overline">2</td></tr></table></td>
#<td>,</td>
#<td><table class="frac"><tr><td>1</td></tr><tr><td class="overline">7</td></tr></table></td>
#<td>,</td>
#<td><table class="frac"><tr><td>55</td></tr><tr><td class="overline">1</td></tr></table></td>
#<td>.</td>
#</tr></table>Starting with the seed integer 2, successive iterations of the program produce the sequence:
#15, 825, 725, 1925, 2275, 425, ..., 68, 4, 30, ..., 136, 8, 60, ..., 544, 32, 240, ...
#The powers of 2 that appear in this sequence are 2^2, 23, 25, ...
#It can be shown that all the powers of 2 in this sequence have prime exponents and that all the primes appear as exponents of powers of 2, in proper order!
#If someone uses the above Fractran program to solve Project Euler Problem 7 (find the 10001st prime), how many iterations would be needed until the program produces 2^10001st prime ?
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))