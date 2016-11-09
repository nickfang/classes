# Poker hands

#
#In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
#<ul><li>High Card: Highest value card.</li>
#<li>One Pair: Two cards of the same value.</li>
#<li>Two Pairs: Two different pairs.</li>
#<li>Three of a Kind: Three cards of the same value.</li>
#<li>Straight: All cards are consecutive values.</li>
#<li>Flush: All cards of the same suit.</li>
#<li>Full House: Three of a kind and a pair.</li>
#<li>Four of a Kind: Four cards of the same value.</li>
#<li>Straight Flush: All cards are consecutive values of same suit.</li>
#<li>Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.</li>
#</ul>The cards are valued in the order:2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.
#Consider the following five hands dealt to two players:
#
#<table><tr><td>Hand</td><td> </td><td>Player 1</td><td> </td><td>Player 2</td><td> </td><td>Winner</td>
#</tr><tr><td style="vertical-align:top;">1</td><td> </td><td>5H 5C 6S 7S KDPair of Fives</td><td> </td><td>2C 3S 8S 8D TDPair of Eights</td><td> </td><td style="vertical-align:top;">Player 2</td>
#</tr><tr><td style="vertical-align:top;">2</td><td> </td><td>5D 8C 9S JS ACHighest card Ace</td><td> </td><td>2C 5C 7D 8S QHHighest card Queen</td><td> </td><td style="vertical-align:top;">Player 1</td>
#</tr><tr><td style="vertical-align:top;">3</td><td> </td><td>2D 9C AS AH ACThree Aces</td><td> </td><td>3D 6D 7D TD QDFlush  with Diamonds</td><td> </td><td style="vertical-align:top;">Player 2</td>
#</tr><tr><td style="vertical-align:top;">4</td><td> </td><td>4D 6S 9H QH QCPair of QueensHighest card Nine</td><td> </td><td>3D 6D 7H QD QSPair of QueensHighest card Seven</td><td> </td><td style="vertical-align:top;">Player 1</td>
#</tr><tr><td style="vertical-align:top;">5</td><td> </td><td>2H 2D 4C 4D 4SFull HouseWith Three Fours</td><td> </td><td>3C 3D 3S 9S 9DFull Housewith Three Threes</td><td> </td><td style="vertical-align:top;">Player 1</td>
#</tr></table>
#The file, <a href="project/resources/p054_poker.txt">poker.txt</a>, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
#How many hands does Player 1 win?
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))