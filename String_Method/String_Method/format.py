# Demonstrating the use of the format() method in Python
# The format() method allows you to format strings by inserting variables into placeholders.

# Example 1: Using positional arguments in format()
name = "Kibrom"
age = 22
message = "My name is {0} and I am {1} years old. {1} is my favorite number.".format(
    name, age)
print(message)
# Expected output: My name is Kibrom and I am 22 years old. 22 is my favorite number.

# Example 2: Using named arguments in format()
txt = "I have {an:.2f} Rupees!"
print(txt.format(an=4))
# Expected output: I have 4.00 Rupees!
