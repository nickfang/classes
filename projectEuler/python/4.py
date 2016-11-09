#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome (num):
   numString = str(num)
   for x in range (len(numString)/2):
      if numString[x] != numString[-1-x]:
         return False
   return True

candidate = 0
for x in range(1000)[1000:1:-1]:
   for y in range(1000)[1000:1:-1]:
      if (x*y) > candidate:
         if isPalindrome(x*y):
            candidate = x*y

print candidate
