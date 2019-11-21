#Exercise on array calculations and operations
 
import numpy as np

a = np.array([range(4), range(10,14)])

b = np.array([2,-1,1,0])

#multiply a and b

print(a*b)

#multiply array b by 100
b1 = b*100

#multiply array b by 100.0

b2 = b*100.0

#are b1 and b2 the same? 

print(b1 == b2)

#look at data type for b1 and b2

print(b1.dtype, b2.dtype)

#create an array between 0-9

arr = np.array([range(10)])

#print two different ways of expressing the condition where array < 3

print(arr<3)

print(np.less(arr,3))

#create a numpy condition where "arr" is less than 3 and greater than 8

condition = np.logical_or(arr<3,arr>8)

#use the "where" function to create array value is "a*5" if condition is true and "a-5" if condition is false

new_arr = np.where(condition, a*5, a-5)

print(new_arr)

#Mathematical function on arrays

#Write function described in the exercise sheet



