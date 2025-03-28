# Remove punctuation
import string

string_1 = "Hello, World! Welcome to Python."
tab = str.maketrans("", "", string.punctuation)
result = string_1.translate(tab)
print(result)
