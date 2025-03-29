# Demonstrating the use of the expandtabs() method in Python
# The expandtabs() method replaces tab characters ('\t') in a string with spaces.
# By default, the tab size is 8 spaces, but it can be customized.

# Example 1: Expanding tabs with the default spacing
string = "Name\tAge\tLocation"
result = string.expandtabs()
print(result)
# Expected output:
# Name      Age       Location

# Example 2: Expanding tabs with the default tab size
string_2 = "A\tB\tC"
result_2 = string_2.expandtabs()
print(result_2)
# Expected output:
# A       B       C

# Example 3: Expanding tabs with a custom tab size of 5 spaces
string_3 = "A\tBC\tDEFG"
result_3 = string_3.expandtabs(5)
print(result_3)
# Expected output:
# A     BC    DEFG
