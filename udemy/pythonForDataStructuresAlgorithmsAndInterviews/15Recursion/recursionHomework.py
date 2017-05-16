# write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer
def recursiveSum(n):
	if n == 0:
		return 0
	else:
		return n + recursiveSum(n-1)

print(recursiveSum(4))

# given an integer, create a function which returns the sum of all the individual digits in that integer.
def sumFunction(n):
	if n < 10:
		return n
	else:
		return n%10 + sumFunction(n//10)

print(sumFunction(43215))

#TODO: come back and look at this amd make it work for overlapping words
# this solution doesn't work
def wordSplit(phrase, listOfWords, output = None):
	if phrase == "":
		return output
	for word in listOfWords:
		# if the word is not found return
		leftWord = phrase.split(word)
		if len(leftWord) == 1:
			wordSplit("", [], [])
		else:
			if output == None:
				output = [word]
			else:
				output.append(word)
			wordSplit("".join(leftWord), listOfWords, output)

# from solution >>
# this solution doesn't take into account overlapping words. Actually, thie keeps you from splitting a word into a non word
def wordSplit2(phrase, listOfWords, output = None):
	if output is None:
		output = []
	for word in listOfWords:
		if phrase.startswith(word):
			output.append(word)
			# print(phrase[len(word):], listOfWords, output)
			return wordSplit2(phrase[len(word):], listOfWords, output)
		# print(word)
	return output

# << solution

# Create a function called wordSplit() which takes in a string phtase and set listOfWords.  The function will then determine if it is possible to split the string in a way in which words can be made form the list of words.  You can assume the phrase will only contain words found in the dictionary if it is completely splittable.
# ["the", "man", "ran"]
print(wordSplit2("themanran", ["the", "ran", "man"]))
# ["i", "love", "dogs", "John"]
print(wordSplit2("ilovedogsJohn", ["i", "am", "a", "dogs", "lover", "love", "John"]))
# []
print(wordSplit2("themanran", ["clown", "ran", "man"]))
