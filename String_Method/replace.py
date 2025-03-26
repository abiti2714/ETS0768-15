# Demonstrating the use of the replace() method in Python
# The replace() method replaces occurrences of a substring with another substring.
# It can also limit the number of replacements using an optional count parameter.

# Example 1: Replacing a substring with a limit on the number of replacements
string = "apple apple apple"
# Replace "apple" with "orange" only once
string_2 = string.replace("apple", "orange", 1)
print(string_2)
# Expected output: "orange apple apple"

# Example 2: Replacing all occurrences of a substring
string_3 = "apple apple apple"
# Replace all occurrences of "apple" with "orange"
string_4 = string_3.replace("apple", "orange")
print(string_4)
# Expected output: "orange orange orange"
