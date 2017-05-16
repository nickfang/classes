# give an integer array, output all the unique pairs that sum up to a specific value k

import itertools

def pair_sum(arr, k):
	pairs = set()
	for itr in itertools.combinations(arr, 2):
		if itr[0] + itr[1] == k:
			pairs.add((min(itr[0], itr[1]), max(itr[0], itr[1])))
			print(itr)

	return len(pairs)

pair_sum([1,3,2,2], 4)

# from solution >>
def pair_sum1(arr,k):
	if len(arr) < 2:
		return
	#sets for tracking
	seen = set()
	output = set()

	for num in arr:
		target = k-num
		if target not in seen:
			seen.add(num)
		else:
			output.add( (min(num, target)), max(num, target) )

	return len(output)
# << from solution

"""
Run This Cell to Test Your Solution
"""

from nose.tools import assert_equal

class TestPair(object):
	def test(self, sol):
		assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10), 6)
		assert_equal(sol([1,2,3,1],3),1)
		assert_equal(sol([1,3,2,2],4),2)
		print("All Test Cases Passed")

# run tests
t = TestPair()
t.test(pair_sum)