import re
import exerciseUtils as eu
# data = []

# # read data from a file that has a word per line.
# with open ("words.txt", "r") as myfile:
# 	for line in myfile.readlines():
# 		data.append(line.replace("\n", ""))

# def searchWords(regex):
# 	output = []
# 	for word in data:
# 		if regex.findall(word):
# 			output.append(word)
# 	return output

# Find all words in the dictionary that contain two consonants (i.e., non-vowels), two vowels, and then either "p" or "r". These letters should be consecutive, and can be at the beginning, middle, or end of a word.
match1 = re.compile(r"[^aeiou]{2}[aeiou]{2}[pr]")
print("Output1:", eu.searchWords(match1))

# Find all words that contain "e", "f", "g", and/or "h" three times in a row, then any letter, and then "m", "n", and/or "o" twice in a row.
match2 = re.compile(r"[efgh]{3}\w[mno]{3}")
print("Output2:", eu.searchWords(match2))

# Find words that contain a "q" followed by something other than "u".
match3 = re.compile(r"q[^u]")
print("Output3:", eu.searchWords(match3))
