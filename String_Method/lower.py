# Example 1: Converting uppercase letters to lowercase
string_1 = "Hello, World! "

# Change only uppercase letters to lowercase
result = string_1.lower()
print(result)  # Expected output: hello, world!

# Example 2: Case-insensitive string comparison
string_2 = "Python"
string_3 = "python"

# Convert both strings to lowercase and compare
if string_2.lower() == string_3.lower():
    print("The strings are equal.")  # Expected output: The strings are equal.
else:
    print("The strings are not equal.")

# Note: Non-alphabetic characters remain unchanged in the lower() method.
