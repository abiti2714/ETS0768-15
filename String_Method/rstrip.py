# Demonstrating the use of the rstrip() method in Python
# The rstrip() method removes any trailing characters (specified as an argument) from the end of the string.
# If no argument is provided, it removes trailing whitespace by default.

# Example: Removing specific characters from the end of a string
s = '  ##*#Hello Python!#**##  '

# Removes all occurrences of '#', '*', and ' ' from the end of the string
res = s.rstrip('#* ')
print(res)
# Expected output: "  ##*#Hello Python!"
