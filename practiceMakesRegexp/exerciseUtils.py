import re

def searchWords(regex):
	data = []
	output = []
	# read data from a file that has a word per line.
	with open ("words.txt", "r") as myfile:
		for line in myfile.readlines():
			data.append(line.replace("\n", ""))
	for word in data:
		if regex.findall(word):
			output.append(word)
	return output