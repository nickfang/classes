class Stack(object):
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		if len(self.items) == 0:
			return None
		else:
			return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

def balanceCheck(s):
	if len(s)%2 != 0:
		return False
	stack = Stack()
	for char in s:
		if char in ["[","{","("]:
			stack.push(char)
		else:
			if stack.size() == 0:
				return False
			lastOpen = stack.pop()
			if lastOpen == "[" and char != "]":
				return False
			elif lastOpen == "{" and char != "}":
				return False
			elif lastOpen == "(" and char != ")":
				return False
	return stack.isEmpty()

# solution >>
def balanceCheck2(s):
	if len(s)%2 != 0:
		return False
	opening = set("({[")
	matches = set( [ ("{", "}"), ("[", "]"), ("(", ")") ] )

	stack = []

	for char in s:
		if char in opening:
			stack.append(char)
		else:
			if len(stack) == 0:
				return False
			lastOpen = stack.pop()

			if (lastOpen, char) not in matches:
				return False
	return len(stack) == 0

# << solution

# True
print(balanceCheck("[]"))
# True
print(balanceCheck("[](){([[[]]])}"))
# False
print(balanceCheck("()(){]}"))

"""
Run this cell to test your solution
"""
from nose.tools import assert_equal

class TestBalanceCheck(object):
	def test(self, sol):
		assert_equal(sol("[](){([[[]]])}("), False)
		assert_equal(sol("[{{{(())}}}]((()))"), True)
		assert_equal(sol("[[[]])]"), False)
		print("All Test Cases Passed")

# run tests
t = TestBalanceCheck()
t.test(balanceCheck2)