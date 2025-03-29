# Example 1: Using endswith() to check the ending of a string
# The endswith() method checks if the string ends with the specified suffix.
string_1 = "kibromNasirHalil"
result = string_1.endswith("Halil")  # Corrected variable name and suffix
print(result)  # Expected output: True

# Example 2: Using endswith() to validate file extensions
# Check if the file name ends with '.jpg' or '.png'
file = "profile_picture.jpg"
if file.endswith((".jpg", ".png")):
    print("File is valid!")  # Expected output: File is valid!
else:
    print("Invalid file type!")
