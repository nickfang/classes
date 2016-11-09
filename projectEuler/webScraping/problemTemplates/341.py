# Golomb's self-describing sequence

#
#The Golomb's self-describing sequence {G(n)} is the only nondecreasing sequence of natural numbers such that n appears exactly G(n) times in the sequence. The values of G(n) for the first few n are
#
#<table cellspacing="1" cellpadding="5" border="0" align="center"><tr><td align="left">n</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>…</td></tr><tr><td>G(n)</td><td>1</td><td>2</td><td>2</td><td>3</td><td>3</td><td>4</td><td>4</td><td>4</td><td>5</td><td>5</td><td>5</td><td>6</td><td>6</td><td>6</td><td>6</td><td>…</td></tr></table>
#You are given that G(10^3) = 86, G(106) = 6137.
#You are also given that ΣG(n^3) = 153506976 for 1 ≤ n &lt; 103.
#Find ΣG(n^3) for 1 ≤ n &lt; 106.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))