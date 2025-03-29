# Demonstrating the use of the count() method in Python
# The count() method returns the number of occurrences of a substring in a string.

# Example 1: Counting occurrences of a character
string_1 = "hello world"
result = string_1.count("o")
print(result)  # Expected output: 2

# Example 2: Counting occurrences of a word
string_2 = "Python is fun and Python is powerful."
print(string_2.count("Python"))  # Expected output: 2

# Example 3: Using start and end parameters
# Count occurrences of "apple" within a specific range
string_3 = "apple banana apple grape apple"
substring = "apple"
result_2 = string_3.count(substring, 1, 20)
print(result_2)  # Expected output: 1
