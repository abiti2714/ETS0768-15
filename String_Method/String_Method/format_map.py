# Example 1
# input stored in variable a.
string = {'x': 'John', 'y': 'Wick'}

# Use of format_map() function
print("{x}'s last name is {y}".format_map(string))
# Example 2
# Input dictionary
profession = {'name': ['Barry', 'Bruce'],
              'profession': ['Engineer', 'Doctor'],
              'age': [30, 31]}

# Use of format_map() function
print('{name[0]} is an {profession[0]} and he'
      ' is {age[0]} years old.'.format_map(profession))

print('{name[1]} is an {profession[1]} and he'
      ' is {age[1]} years old.'.format_map(profession))
# Demonstrating the use of the format_map() method in Python
# The format_map() method is used to format strings using a dictionary.

# Example 1: Using format_map() with a simple dictionary
# Input dictionary
string = {'x': 'John', 'y': 'Wick'}

# Use of format_map() function
print("{x}'s last name is {y}".format_map(string))
# Expected output: "John's last name is Wick"

# Example 2: Using format_map() with a nested dictionary
# Input dictionary
data = {
    'name': ['Barry', 'Bruce'],
    'profession': ['Engineer', 'Doctor'],
    'age': [30, 31]
}

# Use of format_map() function
print('{name[0]} is an {profession[0]} and he is {age[0]} years old.'.format_map(data))
# Expected output: "Barry is an Engineer and he is 30 years old."

print('{name[1]} is an {profession[1]} and he is {age[1]} years old.'.format_map(data))
# Expected output: "Bruce is a Doctor and he is 31 years old."
