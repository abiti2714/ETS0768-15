# Python code to get the difference between two sets
# using difference_update() between set A and set B

# Driver Code
A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}

# Modifies A and returns None
A.difference_update(B)

# Prints the modified set
print(A)
