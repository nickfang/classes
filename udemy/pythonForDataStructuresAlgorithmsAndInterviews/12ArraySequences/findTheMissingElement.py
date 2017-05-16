def finder1(arr1, arr2):
	for itr in arr2:
		arr1.remove(itr)
	return arr1[0]

# from solution >>>
def finder2(arr1, arr2):
	arr1.sort()
	arr2.sort()
	for num1, num2 in zip(arr1, arr2):
		if num1 != num2:
			return num1
	return arr1[-1]

import collections
def finder3(arr1, arr2):
	d = collections.defaultdict(int)
	for num in arr2:
		d[num] += 1
	for num in arr1:
		if d[num] == 0:
			return num
		else:
			d[num] -= 1

def finder(arr1, arr2):
	result = 0
	# perform an XOR between the numbers in the arrays
	for num in arr1+arr2:
		result ^= num
		print(num)
	return result
# <<< from solution

"""
Run This Cell to Test Your Solution
"""
from nose.tools import assert_equal

class TestFinder(object):
	def test(self, sol):
		assert_equal(sol([5,5,7,7],[5,7,7]), 5)
		assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]), 5)
		assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]), 6)
		print("All Test Cases Passed")

# Run Test
t = TestFinder()
t.test(finder)