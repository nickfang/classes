isPrime = [1] * 2000000 
value = 2 
s = 0
while value < 2000000: 
   if isPrime[value] == 1: 
      s += value 
      i = value 
      while i < 2000000: 
         isPrime[i] = 0 
         i += value 
   value += 1 
print s
