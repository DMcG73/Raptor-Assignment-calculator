import random
import math
import numpy

success = False
xarray = numpy.zeros(999)
for i in range(1,1000):
    x=1
    while(not success):
        y=math.floor(100/x)
        if(random.randint(1,y)==1):
            success = True
        else:
            x+=1
    xarray[i-1] = x
    success = False

print("average amount of tasks: ", numpy.mean(xarray))
print("minimum amount of tasks: ", min(xarray))
print("maximum amount of tasks: ", max(xarray))
