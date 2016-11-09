#A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#
#a2 + b2 = c2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
# a = m^2-n^2
# b = 2mn
# c = m^2+n^2
# 500 = m^2+mn = m(m+n)
# m has to be greater than n since a is positive.
# 500/m = m+n
# (500/m)-m = n
# keep increasing m until is is greater than n and n is an integer

def pythtriple(m, n):
    """ Returns values for a,b,c and where a^2 + b^2 = c^2 for a given
    m and n where m and n > 0, and m > n """
    if m <= n or m <= 0 or n <= 0 :
        raise ValueError("m and n must be postiive, and m > n")
    a = m*m - n*n
    b = 2 * m * n
    c = m*m + n*n

    return(a,b,c)

def pythtriplesum(n):
    """ Yields the sum of a pythagorean triple in range n """
    for i in range(1,n):
        for j in range(i+1,n):
            triple = pythtriple(j,i)
            yield(triple, sum(triple))

def productlist(seq):
    """ multiplies all numbers in a sequence"""
    product = 1 
    for i in seq:
        product *= i
    return product

for i in pythtriplesum(1000):
   if i[1] == 1000:
      print("Pythagorean Triple: ", i[0], " Product: ", productlist(i[0]))


