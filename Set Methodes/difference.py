# Example 1
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
C = {5, 6, 7, 8, 9}

result = A.difference(B, C)  # Elements in A that are not in B or C
print(result)
# Example 2
A = {10, 20, 30, 40, 80}
B = {10, 20, 30, 40, 80, 100}

print(A.difference(B))  # Returns an empty set as A is fully contained in B
