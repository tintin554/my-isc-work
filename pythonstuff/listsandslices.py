forward = []
backward = []
values = ["a", "b", "c"]

#for loop

for value in values :
    forward.append(value)
    backward.insert(0, value)

print("forward is", forward)
print("backward is", backward)
