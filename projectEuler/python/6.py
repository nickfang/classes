#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumOfSquare(num):
   total = 0 
   for x in range(num+1):
      total = total + (x * x)
   return total
   
def squareOfSum(num):
   total = sum(range(num+1))
   total = total * total
   return total
#sum([x for x in range(101)])**2 - sum([x**2 for x in range(101)])
x = 100
print (squareOfSum(x) - sumOfSquare(x))
