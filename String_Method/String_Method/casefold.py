# Example: Using casefold() to transform a string to lowercase
# Define the original string
string = "WeightAGE oF THe DiScuSSiON"

# Print the original string
# Expected output: 'WeightAGE oF THe DiScuSSiON'
print("Original String:", string)

# Print the string after casefold transformation
# casefold() is more aggressive than lower() and is used for caseless matching
print("String after using casefold():", string.casefold())
# Expected output: 'weightage of the discussion'
