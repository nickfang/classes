def large_cont_sum(arr):
	max = 0
	for x in range(len(arr)):
		sum = 0
		for y in range(len(arr) - x):
			sum += arr[x+y]
			if sum > max:
				max = sum
	return max

# from solution >>>
def large_cont_sum2(arr):
	if len(arr) == 0:
		return 0
	max_sum = current_sum = arr[0]
	for num in arr[1:]:
		current_sum = max(current_sum + num, num)
		max_sum = max(current_sum, max_sum)

	return max_sum
# <<< from solution

"""
Run This Cell to Test Your Solution
"""
from nose.tools import assert_equal

class LargeContTest(object):
	def test(self, sol):
		assert_equal(sol([1,2,-1,3,4,-1]), 9)
		assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]), 29)
		assert_equal(sol([-1,1]), 1)
		print("All Test Cases Passed")

# Run Test
t = LargeContTest()
t.test(large_cont_sum2)