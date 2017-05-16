# TODO: try to get beginning and ending index that created the output
def compress(s):
	if len(s) == 0:
		return ""

	s = sorted(s)
	lastLetter = s[0]
	numLetter = 1
	output = ""
	for char in s[1:]:
		if char == lastLetter:
			numLetter += 1
		else:
			output += lastLetter + str(numLetter)
			numLetter = 1
			lastLetter = char
	output += lastLetter + str(numLetter)
	return output

# solution >>
def compress2(s):
	r = ""
	l = len(s)
	if l == 0:
		return ""
	if l == 1:
		return s+"1"
	last = s[0]
	cnt = 1
	i = 1

	while i < l:
		if s[i] == s[i-1]:
			cnt += 1
		else:
			r = r + s[i-1] + str(cnt)
			cnt = 1
		i += 1
	r = r + s[i - 1] + str(cnt)
	return r

# << solution

"""
Run This Cell to Test Your Solution
"""
from nose.tools import assert_equal

class CompressTest(object):
	def test(self, sol):
		assert_equal(sol(""), "")
		assert_equal(sol("A"), "A1")
		assert_equal(sol("AABBCC"), "A2B2C2")
		assert_equal(sol("AAABCCDDDDD"), "A3B1C2D5")
		print("All Test Cases Passed")

# Run Tests
t = CompressTest()
t.test(compress)