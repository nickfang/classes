# Implement a Fibonnaci Sequence in three different ways: Recursively, Dynamically (using Memoization) and iteratively

# Your function will accept a number and return the nth number of the fibonacci sequence
# Remember that a a fibonacci sequnce: 0, 1, 1, 2, 3, 5, 8, 13, 21, ... starts off with a base case checking to see if n = 0 or 1 then it returns 1
# Else it returns fib(n-1) + fib(n-2)

# Recursively
def fibRec(n):
	if n == 0 or n == 1:
		return n
	else:
		return fibRec(n - 1) + fibRec(n - 2)

# 55
print(fibRec(23))



# Dynamically
n = 23
cache = [None] * (n+1)
cache[0] = 0
cache[1] = cache[2] = 1
def fibDyn(n):
	if cache[n]:
		return cache[n]
	else:
		cache[n] = fibDyn(n-1) + fibDyn(n-2)
	return cache[n]

# 55
print(fibDyn(10))



def fibItr(n):
	last1 = last2 = 1
	if n == 1 or n == 2:
		return 1
	for i in range(n-2):
		temp = last2
		last2 = last1
		last1 = temp + last2
	return last1

# 55
print(fibItr(10))

# solution >>
# https://technobeans.com/2012/04/16/5-ways-of-fibonacci-in-python/

def fib_rec(n):
	# base case
	if n == 0 or n == 1:
		return n
	# recursive case
	else:
		return fib_rec(n-1) + fib_rec(n-2)

# cache
n = 10
cache = [None] * (n+1)

def fib_dyn(n):
	# base case
	if n == 0 or n == 1:
		return n
	# check cache
	if cache[n] != None:
		return cache[n]
	# keep setting cache  can use append to add to cache probably need to check cache is too small above.
	cache[n] = fib_dyn(n-1) + fib_dyn(n-1)
	return cache[n]

# uses tuple unpacking
def fib_itr(n):
	a,b = 0,1
	for i in range(n):
		a,b = b, a+b
	return a

# << solution

"""
Run This Cell to Test Your Solution
"""

from nose.tools import assert_equal

class TestFib(object):
	def test(self, solution):
		assert_equal(solution(10), 55)
		assert_equal(solution(1), 1)
		assert_equal(solution(23), 28657)
		print("All Test Cases Passed")

# Run Tests
t = TestFib()
t.test(fibRec)
t.test(fibDyn)
t.test(fibItr)