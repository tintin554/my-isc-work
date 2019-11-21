# Sets and dictionaries exersize 

#create sets

a = set([0, 1, 2, 3, 4, 5])
b = set([2, 4, 6, 8])

#print union of a and b

print(a.union(b))

#OR

print(a | b) #shorthand

#print intersection between two sets

print(a.intersection(b))

# Using a dictionary to collect up counts

#making a list

band = ["mel", "geri", "victoria", "mel", "emma"]

#empty dictionary

counts = { }

#Loop to add each member to dictionary and printprint

for member in band :
    if member not in counts :
        counts[member] = 1
    else :
        counts[member] += 1
        print(member, 'has been spotted again')

