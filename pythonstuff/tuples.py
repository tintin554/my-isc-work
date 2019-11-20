# tuple creation
t = (1,)

#print last value

print(t[-1])

#tuple a range from 100-200

r = range(100, 201)

tuple(r)

#print first and last

print(r[0])
print(r[-1])

# using the enumerate function to look at indexes and values 

mylist = [23, "hi", 2.4e-10]

for (count, item) in enumerate(mylist) :
    pint(count, item)

#the print assigns each value as a tuple 

