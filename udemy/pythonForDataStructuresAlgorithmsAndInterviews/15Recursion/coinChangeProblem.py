# Given a target amount of n and a list (array) of distince coin values, what's the fewest coins needed to make the change amount
# For example:
# if n = 10 and coins = [1, 5, 10].  Then there are 4 possible ways to make change:
# 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
# 5 + 1 + 1 + 1 + 1 + 1
# 5 + 5
# 10
# With 1 coin being the minimum amount

# cache of targets
cache = []

# the solution get's get the min number of coins.  I want to get the list of the min number of coins.
def recCoin(target, coins):
	returnList = []
	minNumCoins = target
	# the target value exactly matches a coin, assign cache[target] to the target value.
	# if it was already assigned, we shouldn't get to here.
	if target in coins:
		cache[target] = [target]
		return cache[target]
	# if the target value is already cached
	elif cache[target]:
		return cache[target]
	else:
		# getting a generator that iterates for each coin who's value is under target's
		for i in (c for c in coins if c <= target):
			# don't forget to include the current coin in the return list (spent several hours trying to figure out why this didn't work)
			returnList = [i] + recCoin(target - i, coins)
			# at this point, we're done recuring, so we just need to make sure this one is less than minNumCoins
			if len(returnList) < minNumCoins:
				minNumCoins = len(returnList)
				cache[target] = returnList
	return(returnList)

cache = [None] * 75
print(recCoin(74, [1,5,10,25]))


# solution >>
# incorrect solution (recalculating many things)
# TODO: look up list comprehension
def recCoin2(target, coins):
	minCoins = target
	if target in coins:
		return 1
	else:
		for i in [c for c in coins if c <= target]:
			numCoins = 1 + recCoin2(target-i, coins)
			if numCoins < minCoins:
				minCoins = numCoins
	return minCoins

# print(recCoin2(15, [1,5,10]))
# << solution

def recCoinDyn(target, coins, cache):
	minCoins = target
	if target in coins:
		cache[target] = 1
		return 1
	elif cache[target] > 0:
		return cache[target]
	else:
		for i in [c for c in coins if c <= target]:
			numCoins = 1 + recCoinDyn(target-i, coins, cache)
			if numCoins < minCoins:
				minCoins = numCoins
				cache[target] = minCoins
	return minCoins

target = 74
coins = [1,5,10,25]
cache = [0] * (target+1)
print(recCoinDyn(target, coins, cache))


"""
Run This Cell to Test Your Function
Note: Non-Dynamic Functions Will Take a Long Time to Test.  If You Believe You Have A Solution
Go Check The Solution Notebook Instead of Runnint This!
"""

from nose.tools import assert_equal

class TestCoins(object):
	def check(self, solution):
		coins = [1,5,10,25]
		assert_equal(solution(45, coins), 3)
		assert_equal(solution(23, coins), 5)
		assert_equal(solution(74, coins), 8)
		print("Passed All Tests.")

# run test
test = TestCoins()
# test.check(recCoin)