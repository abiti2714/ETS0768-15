# Example 1: Centering a String
# Center the string 'hello' within a width of 20
string_1 = "hello"
result = string_1.center(20)

# Print the result
print(result)  # Expected output: '       hello        '

# Example 2: Centering Table Headers
# Define table headers
h1 = "Name"
h2 = "Age"
h3 = "Location"

# Center each header within a width of 20 characters, using '-' as the fill character
s1 = h1.center(20, '-')
s2 = h2.center(20, '-')
s3 = h3.center(20, '-')

# Print the centered headers
print(s1)  # Expected output: '--------Name--------'
print(s2)  # Expected output: '--------Age---------'
print(s3)  # Expected output: '------Location------'
