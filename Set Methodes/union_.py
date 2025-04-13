A = {2, 4, 5, 6}
B = {4, 6, 7, 8}
C = {7, 8, 9, 10}

# using multiple union calls
print("A U B U C:", A.union(B).union(C))

# directly passing multiple sets
print("A U B U C:", A.union(B, C))
