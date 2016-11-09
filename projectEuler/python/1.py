# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

numbers = set([])
i = 0
while (i*3<1000):
   numbers.add(i*3)
   i = i + 1
i = 0
while (i*5<1000):
   numbers.add(i*5)
   i = i+1
total = sum(numbers)
print numbers
print total
