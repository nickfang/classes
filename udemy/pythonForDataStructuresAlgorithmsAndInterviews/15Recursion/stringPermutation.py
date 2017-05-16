# Given a string, write a function that uses recursion to ouput a list of all the possible permutations of that string.

# for example, given s="abc" the function should return ["abc", "acb", "bac", "bca", "cab", "cba"]

def permute(s):
	returnList = []
	if len(s) == 1:
		returnList = [s]
	else:
		for i in range(len(s)):
			for perm in permute(s[0:i] + s[i+1:]):
				returnList += [perm+s[i]]

	return returnList

# solution >>
def permute2(s):
	out = []
	if len(s) == 1:
		out = [s]
	else:
		for i, let in enumerate(s):
			for perm in permute2(s[:i] + s[i+1:]):
				out += [let+perm]
	return out
# << solution

"""
Run This Cell to Test Your Solution
"""

from nose.tools import assert_equal

class TestPerm(object):
	def test(self, solution):
		assert_equal(sorted(solution("abc")), sorted(["abc", "acb", "bac", "bca", "cab", "cba"]))
		assert_equal(sorted(solution("dog")), sorted(["dog", "dgo", "odg", "ogd", "gdo", "god"]))
		print("All Test Cases Passed")

# Run Tests
t=TestPerm()
t.test(permute)