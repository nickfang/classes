def revWords(str):
	words = str.split()
	return " ".join(words[::-1])

# output: go? to ready you are John, Hi
print(revWords("Hi John,   are you ready to go?"))

# output: before space
print(revWords("      space before"))

#
def revWords2(s):
	words = []
	length = len(s)
	spaces = [" "]

	i = 0

	while i < length:
		if s[i] not in spaces:
			word_start = i
			while i < length and s[i] not in spaces:
				i += 1
			words.append(s[word_start:i])
		i += 1
	return " ".join(reversed(words))
#

"""
Run This Cell to Test Your Solution
"""
from nose.tools import assert_equal

class ReversalTest(object):
	def test(self, sol):
		assert_equal(sol("    space before"), "before space")
		assert_equal(sol("space after     "), "after space")
		assert_equal(sol("   Hello John    how are you    "), "you are how John Hello")
		assert_equal(sol("1"), "1")
		print("All Test Cases Passed")

# Run Test
t = ReversalTest()
t.test(revWords2)