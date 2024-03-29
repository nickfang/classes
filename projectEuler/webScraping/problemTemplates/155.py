# Counting Capacitor Circuits

#
#An electric circuit uses exclusively identical capacitors of the same value C.
#
#The capacitors can be connected in series or in parallel to form sub-units, which can then be connected in series or in parallel with other capacitors or other sub-units to form larger sub-units, and so on up to a final circuit.
#Using this simple procedure and up to n identical capacitors, we can make circuits having a range of different total capacitances. For example, using up to n=3 capacitors of 60 <img src="project/images/p155_capsmu.gif" width="12" height="21" alt="" style="vertical-align:middle;" />F each, we can obtain the following 7 distinct total capacitance values: 
#<img src="project/images/p155_capacitors1.gif" width="387" height="557" alt="" />
#If we denote by D(n) the number of distinct total capacitance values we can obtain when using up to n equal-valued capacitors and the simple procedure described above, we have: D(1)=1, D(2)=3, D(3)=7 ...
#Find D(18).
#Reminder : When connecting capacitors C1, C2 etc in parallel, the total capacitance is CT = C1 + C2 +...,
#
#whereas when connecting them in series, the overall capacitance is given by:
#<img src="project/images/p155_capsform.gif" width="127" height="38" alt="" style="vertical-align:middle;" />
#

import time

startTime = time.time()



print('Elapsed time: ' + str(time.time()-startTime))