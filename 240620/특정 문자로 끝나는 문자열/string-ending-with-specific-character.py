# Taking 10 inputs and storing them in list a
a = [input() for _ in range(10)]

# Taking the character b
b = input()

# Initialize a flag to check if any match is found
found = False

# Iterating through each item in the list
for item in a:
    if item[-1] == b:
        print(item)
        found = True

# If no match is found, print 'None'
if not found:
    print('None')