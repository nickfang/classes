# use recursion to reverse a string

def reverse(s):
	if len(s) == 1:
		return s
	else:
		return s[-1] + reverse(s[0:-1])

# solution >>
def reverse2(s):
	# Base Case
	if len(s) <= 1:
		return s
	# Recursion
	return reverse2(s[1:]) + s[0]
# << solution


"""
Run This Cell to Test Your Function Against Some Test Cases
"""

from nose.tools import assert_equal

class TestReverse(object):
	def testReverse(self, solution):
		assert_equal(solution("hello"), "olleh")
		assert_equal(solution("hello world"), "dlrow olleh")
		assert_equal(solution("123456789"), "987654321")

		print("Passed All Test Cases")

# Run Tests
test = TestReverse()
test.testReverse(reverse)