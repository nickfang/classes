# GCD sequence

#
#Let g(n) be a sequence defined as follows:
#g(4) = 13,
#g(n) = g(n-1) + gcd(n, g(n-1)) for n &gt; 4.
#The first few values are:
#
#<table cellspacing="1" cellpadding="5" border="0" align="center"><tr><td>n</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>...</td>
#</tr><tr><td>g(n)</td><td>13</td><td>14</td><td>16</td><td>17</td><td>18</td><td>27</td><td>28</td><td>29</td><td>30</td><td>31</td><td>32</td><td>33</td><td>34</td><td>51</td><td>54</td><td>55</td><td>60</td><td>...</td>
#</tr></table>
#You are given that g(1 000) = 2524 and g(1 000 000) = 2624152.
#Find g(10^15).
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))