import math

# get the divisors of a number not including the number itself.
def getDivisors(n):
	if (n is 1):
		return [1]
	else:
		divisors = []
		# get all integers between 1 and sqrt(n) + 1.  Go through these to get possible factors.
		for x in range(1,math.floor(n ** 0.5)+1):
			if ((n % x) == 0):
				divisors.append(x)
		# get the rest of the factors by dividing the
		for x in reversed(divisors):
			if (x != int(n / x)):
				divisors.append(int(n / x))
		# remove (n / 1)
		divisors.pop()
		return divisors