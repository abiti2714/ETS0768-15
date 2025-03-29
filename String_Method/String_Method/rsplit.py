# Demonstrating the use of the rsplit() method in Python
# The rsplit() method splits a string into a list, starting from the right.
# It takes two arguments: the delimiter and the maximum number of splits.

# Example 1: Splitting at the last occurrence of a delimiter
word = 'addis, ababa, university'
# Splits the string at the last occurrence of ',' with a maximum of 1 split
result = word.rsplit(',', 1)
print(result)
# Expected output: ['addis, ababa', ' university']

# Example 2: Splitting at '@' with a maximum of 1 split
word = 'addis@ababa@university'
result = word.rsplit('@', 1)
print(result)
# Expected output: ['addis@ababa', 'university']
