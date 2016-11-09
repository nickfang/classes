#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def factor(n):
   i = 2
   limit = n**0.5
   while i <= limit:
      if n % i == 0:
        yield i
        n = n / i
        limit = n**0.5
      else:
        i += 1
   if n > 1:
      yield n

print [i for i in factor(600851475143)]
