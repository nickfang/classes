def anagram(s1, s2):
	s1 = s1.replace(" ", "").lower()
	s2 = s2.replace(" ", "").lower()
	for char in s1:
		s2temp = s2.replace(char, "", 1)
		# if nothing is removed, return false
		if s2temp == s2:
			return False
		s2 = s2temp
	# if s2 is not empty it had extra letters from s1
	if s2 == "":
		return True
	else:
		return False

# from solution >>
def anagram2(s1, s2):
	s1 = s1.replace(" ", "").lower()
	s2 = s2.replace(" ", "").lower()
	return sorted(s1) == sorted(s2)

def anagram3(s1, s2):
	s1 = s1.replace(" ", "").lower()
	s2 = s2.replace(" ", "").lower()

	if len(s1) != len(s2):
		return False

	count = {}
	for char in s1:
		if char in count:
			count[char] += 1
		else:
			count[char] = 1

	for char in s2:
		if char in count:
			count[char] -= 1
		else:
			count[char] = 1

	for itr in count:
		if count[itr] != 0:
			return False
	return True
# << from solution


# should output true
print(anagram('dog', 'god'))
# should output true
print(anagram('clint eastwood', 'old west action'))
# should output false
print(anagram('aa', 'bb'))

"""
Run This Cell to Test Your Solution
"""

from nose.tools import assert_equal

class AnagramTest(object):
	def test(self, sol):
		assert_equal(sol('go go go', 'gggooo'),True)
		assert_equal(sol('abc', 'cba'),True)
		assert_equal(sol('hi man', 'hi     man'),True)
		assert_equal(sol('aabbcc', 'aabbc'),False)
		assert_equal(sol('123', '1 2'),False)
		print("All Test Cases Passed")

# Run Tests
t = AnagramTest()
t.test(anagram)
