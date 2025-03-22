# Demonstrating the use of the find() method in Python
# The find() method returns the lowest index of the substring if it is found in the string.
# If the substring is not found, it returns -1.

# Example 1: Finding the index of a substring
string = "Welcome to GeekforGeeks!"
index = string.find("GeekforGeeks")
print(index)
# Expected output: 11

# Example 2: Using the start parameter in find()
# Find the substring "abc" starting from index 4
string_2 = "abc abc abc"
index_2 = string_2.find("abc", 4)
print(index_2)
# Expected output: 8
