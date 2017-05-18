input = [1,2,3,4]
product = [1,1,1,1]
for x in range(len(input)):
   for itr in input[0:x]+input[x+1:]:
      product[x] *= itr
print(product)