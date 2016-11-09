#Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# +--+--+     +--+  +     +--+  +
#       |        |           |  
# +  +  +     +  +--+     +  +  +
#       |           |        |  
# +  +  v     +  +  v     +  +-->
  

# +  +  +     +  +  +     +  +  +
# |           |           |    
# +--+--+     +--+  +     +  +  +
#       |        |        |    
# +  +  v     +  +-->     +--+-->

#How many such routes are there through a 20x20 grid?

#from http://code.jasonbhill.com/python/project-euler-problem-15/
import time
def route_num(cube_size):
    L = [1] * cube_size
    for i in range(cube_size):
        for j in range(i): # for j in range(0) does not run anything in the loop.
            L[j] = L[j]+L[j-1]
        L[i] = 2 * L[i - 1]
    return L[cube_size - 1]
 
start = time.time()
n = route_num(20)
elapsed = (time.time() - start)
print "%s found in %s seconds" % (n,elapsed)

#from https://alphacentauri32.wordpress.com/2012/06/27/project-euler-problem-15-solved-with-python/
from math import factorial
 
def main():
    """Main Program"""
    start_time = time.time()
 
    n = 40      # The total number of moves for any one path (right + down)
    r = 20      # The total number of right moves for any one path
 
    print factorial(n) / (factorial(r) * factorial(n - r))
    print "Elapsed Time:", (time.time() - start_time) * 1000, "millisecs"
 
if __name__ == '__main__':
    main()
