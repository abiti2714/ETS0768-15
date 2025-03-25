# Demonstrating the use of the strip() method in Python
# The strip() method removes any leading and trailing characters (specified as an argument).
# If no argument is provided, it removes leading and trailing whitespace by default.

# Example 1: Removing specific characters from the start and end of a string
string = '  ##*#ElectromechanicalEngineering#**##  '

# Removes all occurrences of '#', '*', and ' ' from the start and end of the string
result = string.strip('#* ')
print(result)
# Expected output: "ElectromechanicalEngineering"
