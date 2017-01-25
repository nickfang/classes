import re
import exerciseUtils as eu

# Find the middle two digits from US-style Social Security numbers (###-##-####)
print(re.search(r"\d{3}-(\d{2})-\d{4}", "111-22-3333").group(1))

# Find all words in the dictionary that start with "ex" and end, optionally, with "ing".
match1 = re.compile(r"^ex.*(ing)?$")
print("Match1: ",eu.searchWords(match1))

# Find all words in which "la" appears at least twice in a row.
laWords = ["lala", "exlaexla", "landlalaland", "exlala", "landing"]
output2 = []
match2 = re.compile(r"(la){2}")
for word in laWords:
	if match2.findall(word):
		output2.append(word)
print("Match2: ", output2)

# In words containing "la" at least twice in a row, find the first two letters.
output3 = []
match3 = re.compile(r"(^\w{2})")
for word in output2:
	output3.append(match3.findall(word))
print("Match3: ", output3)