# Example 1: Using capitalize() on a string with multiple words
# The capitalize() method converts the first character of the string to uppercase
# and the rest of the string to lowercase.
string_1 = "multiple WORDS IN a String"
result = string_1.capitalize()
print(result)  # Expected output: 'Multiple words in a string'

# Example 2: Using capitalize() on a string starting with a number
# If the string starts with a non-alphabetic character, capitalize() has no effect on it.
string_2 = "123hello WORLD"
result_2 = string_2.capitalize()
print(result_2)  # Expected output: '123hello world'
