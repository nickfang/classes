# Names scores

#
#Using <a href="project/resources/p022_names.txt">names.txt</a> (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 Ă&mdash; 53 = 49714.
#What is the total of all the name scores in the file?
#

import time

startTime = time.time()


def sumLetters(name):
	sum = 0
	letterValues = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for char in name:
		sum += letterValues.index(char) + 1
	return sum

with open ("022_names.txt", "r") as file:
	# remove all the "" and then split each name into an array element using the , as a divider
	names = file.read().replace('"','').split(",")
	# .sort is done in place and is a little faster than sorted()
	names.sort()
	total = 0
	for x in range(len(names)):
		total += (x + 1) * sumLetters(names[x])
	print("Total name scores: ", total)

print('Elapsed time: ' + str(time.time()-startTime))