#NumPy arrays intro exercises

import numpy as np

# make list 1-10

x = range(1,11)

# create integer array of x

x1 = np.array(x, np.int32)

# create floats array of x

x2 = np.array(x, np.float32)

# print data type of each array 

print(a1.dtype)

print(a2.dtype)

#create array of zeros shape (2,3,4)

np.zeros((2,3,4))

# create array of ones shape (2,3,4)

np.ones((2,3,4))

#create array of values between 0 and 999 using np.arange fn

np.arange(0,1000)

