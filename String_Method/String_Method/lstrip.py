# Demonstrating the use of the lstrip() method in Python
# The lstrip() method removes any leading characters (specified as an argument) from the start of the string.
# If no argument is provided, it removes leading whitespace by default.

# Example 1: Removing leading whitespace
string = "   Hello Python!     "
result = string.lstrip()
print(result)
# Expected output: "Hello Python!     "

# Example 2: Removing specific characters from the start of the string
string_2 = '  ##*#Hello Python!#**##  '

# Removes all occurrences of '#', '*', and ' ' from the start of the string
result_2 = string_2.lstrip('#* ')
print(result_2)
# Expected output: "Hello Python!#**##  "
