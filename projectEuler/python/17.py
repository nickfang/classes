#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

import inflect
import re
import time

startTime = time.time()

p = inflect.engine()
totalSize = 0
for x in range(1000):
   numString = p.number_to_words(x+1)
   numString = re.sub('[ -]', '', numString)
   tempSize = len(numString)
   totalSize += tempSize

print totalSize
elapsedTime = time.time() - startTime
print elapsedTime
