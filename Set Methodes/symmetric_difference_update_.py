# Python code to demonstrate working of
# symmetric_difference_update()

A = {'p', 'a', 'w', 'a', 'n'}
B = {'r', 'a', 'o', 'n', 'e'}

# Modifies A in place to contain the symmetric difference
A.symmetric_difference_update(B)

print('A = ', A)  # Expected output: {'p', 'w', 'r', 'o', 'e'}
print('B = ', B)  # Expected output: {'r', 'a', 'o', 'n', 'e'}
