# Demonstrating the use of the index() method in Python
# The index() method returns the index of the first occurrence of a substring in a string.
# If the substring is not found, it raises a ValueError.

# Example 1: Finding the position of a substring
string = "Python programming is powerful"
position = string.index("programming")
print(position)
# Expected output: 7

# Example 2: Using start and end parameters in index()
# Find the substring "is" within the range of index 10 to 25
string_2 = "Python programming is fun"
position = string_2.index("is", 10, 25)
print(position)
# Expected output: 19
