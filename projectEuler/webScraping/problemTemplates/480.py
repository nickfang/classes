# The Last Question

#
#Consider all the words which can be formed by selecting letters, in any order, from the phrase:
#thereisasyetinsufficientdataforameaningfulanswer
#Suppose those with 15 letters or less are listed in alphabetical order and numbered sequentially starting at 1.
#The list would include:
#<ul style="list-style-type:none;"><li>1 : a</li>
#<li>2 : aa</li>
#<li>3 : aaa</li>
#<li>4 : aaaa</li>
#<li>5 : aaaaa</li>
#<li>6 : aaaaaa</li>
#<li>7 : aaaaaac</li>
#<li>8 : aaaaaacd</li>
#<li>9 : aaaaaacde</li>
#<li>10 : aaaaaacdee</li>
#<li>11 : aaaaaacdeee</li>
#<li>12 : aaaaaacdeeee</li>
#<li>13 : aaaaaacdeeeee</li>
#<li>14 : aaaaaacdeeeeee</li>
#<li>15 : aaaaaacdeeeeeef</li>
#<li>16 : aaaaaacdeeeeeeg</li>
#<li>17 : aaaaaacdeeeeeeh</li>
#<li>...</li>
#<li>28 : aaaaaacdeeeeeey</li>
#<li>29 : aaaaaacdeeeeef</li>
#<li>30 : aaaaaacdeeeeefe</li>
#<li>...</li>
#<li>115246685191495242: euleoywuttttsss</li>
#<li>115246685191495243: euler</li>
#<li>115246685191495244: eulera</li>
#<li>...</li>
#<li>525069350231428029: ywuuttttssssrrr</li></ul>Define P(w) as the position of the word w.
#Define W(p) as the word in position p.
#We can see that P(w) and W(p) are inverses: P(W(p)) = p and W(P(w)) = w.
#Examples:
#<ul style="list-style-type:none;"><li>W(10) = aaaaaacdee</li>
#<li>P(aaaaaacdee) = 10</li>
#<li>W(115246685191495243) = euler</li>
#<li>P(euler) = 115246685191495243</li></ul>Find W(P(legionary) + P(calorimeters) - P(annihilate) + P(orchestrated) - P(fluttering)).
#Give your answer using lowercase characters (no punctuation or space).
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))