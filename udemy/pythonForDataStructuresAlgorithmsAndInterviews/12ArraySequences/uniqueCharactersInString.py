def uniChar(arr):
	tempSet = set(sorted(arr))
	if len(tempSet) == len(arr):
		return True
	else:
		return False

# solution >>
def uniChar2(s):
	return len(set(s)) == len(s)

def uniChar3(s):
	char = set()
	for let in s:
		if let in char:
			return False
		else:
			char.add(let)
	return True
# << solution

"""
Run This Cell to Test Your Solution
"""
from nose.tools import assert_equal

class UniqueCharacterTest(object):
	def test(self, sol):
		assert_equal(sol(""), True)
		assert_equal(sol("goo"), False)
		assert_equal(sol("abcdefg"), True)
		print("All Test Cases Passed")

# Run Test
t = UniqueCharacterTest()
t.test(uniChar3)