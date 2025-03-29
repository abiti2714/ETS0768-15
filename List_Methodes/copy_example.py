# Example 1:
import copy

# Original nested list
Number_1 = [[1, 2, 3], [4, 5, 6]]

# Creating a deep copy of the nested list 'Number_1'
Number_2 = copy.deepcopy(Number_1)

# Modifying an element in the deep-copied list
Number_2[0][0] = 99

# Print the deep-copied list
print("Deep Copy (Modified):", Number_2)
# Expected output: [[99, 2, 3], [4, 5, 6]]

# Print the original list to show it remains unchanged
print("Original List:", Number_1)
# Expected output: [[1, 2, 3], [4, 5, 6]]

# Example 2

Number_3 = [[1, 2, 3], [4, 5, 6]]

# Creating a shallow copy of the nested list 'original'
Number_4 = copy.copy(Number_3)

# Modifying an element in the shallow-copied list
Number_4[0][0] = 99

# Printing the original and shallow-copied lists
print(Number_4)
