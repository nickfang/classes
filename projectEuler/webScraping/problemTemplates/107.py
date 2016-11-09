# Minimal network

#
#The following undirected network consists of seven vertices and twelve edges with a total weight of 243.
#
#<img src="project/images/p107_1.gif" width="381" height="278" alt="" />
#The same network can be represented by the matrix below.
#<table cellpadding="5" cellspacing="0" border="1" align="center"><tr><td>    </td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td>
#</tr><tr><td>A</td><td>-</td><td>16</td><td>12</td><td>21</td><td>-</td><td>-</td><td>-</td>
#</tr><tr><td>B</td><td>16</td><td>-</td><td>-</td><td>17</td><td>20</td><td>-</td><td>-</td>
#</tr><tr><td>C</td><td>12</td><td>-</td><td>-</td><td>28</td><td>-</td><td>31</td><td>-</td>
#</tr><tr><td>D</td><td>21</td><td>17</td><td>28</td><td>-</td><td>18</td><td>19</td><td>23</td>
#</tr><tr><td>E</td><td>-</td><td>20</td><td>-</td><td>18</td><td>-</td><td>-</td><td>11</td>
#</tr><tr><td>F</td><td>-</td><td>-</td><td>31</td><td>19</td><td>-</td><td>-</td><td>27</td>
#</tr><tr><td>G</td><td>-</td><td>-</td><td>-</td><td>23</td><td>11</td><td>27</td><td>-</td>
#</tr></table>However, it is possible to optimise the network by removing some edges and still ensure that all points on the network remain connected. The network which achieves the maximum saving is shown below. It has a weight of 93, representing a saving of 243 − 93 = 150 from the original network.
#
#<img src="project/images/p107_2.gif" width="385" height="288" alt="" />
#Using <a href="project/resources/p107_network.txt">network.txt</a> (right click and 'Save Link/Target As...'), a 6K text file containing a network with forty vertices, and given in matrix form, find the maximum saving which can be achieved by removing redundant edges whilst ensuring that the network remains connected.
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))