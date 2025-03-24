# Demonstrating the use of the isdigit() method in Python
# The isdigit() method checks if all characters in a string are digits.
# It returns True if all characters are digits, otherwise False.

# Example 1: String containing only digits
string_1 = "987654"
# Returns True
print(string_1.isdigit())  # Expected output: True

# String with mixed characters (digits and alphabet)
string2 = "987b54"
# Returns False
print(string2.isdigit())  # Expected output: False

# Empty string
string3 = ""
# Returns False
print(string3.isdigit())  # Expected output: False

# Example 2: Unicode digits
# Unicode for '1'
string4 = "\u0031"
# Devanagari digit for '1'
string5 = "\u0967"

# Returns True
print(string4.isdigit())  # Expected output: True

# Returns True
print(string5.isdigit())  # Expected output: True
