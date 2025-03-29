# Example 1: Default Encoding
# The encode() method encodes the string using the default encoding (UTF-8).
string_1 = "Hello, World!"
encoded_text = string_1.encode()
print(encoded_text)  # Expected output: b'Hello, World!'

# Example 2: UTF-8 Encoding
# Explicitly encode the string using UTF-8.
string_2 = "Python is fun!"
utf8_encoded = string_2.encode("utf-8")
print(utf8_encoded)  # Expected output: b'Python is fun!'

# Example 3: ASCII Encoding with Error Handling (replace)
# Encode the string using ASCII and replace non-ASCII characters with '?'.
string_3 = "Pythön"
encoded_ascii = string_3.encode("ascii", errors="replace")
print(encoded_ascii)  # Expected output: b'Pyth?n'

# Example 4: ASCII Encoding with Error Handling (xmlcharrefreplace)
# Encode the string using ASCII and replace non-ASCII characters with XML character references.
string_4 = "Pythön"
encoded_xml = string_4.encode("ascii", errors="xmlcharrefreplace")
print(encoded_xml)  # Expected output: b'Pyth&#246;n'

# Example 5: ASCII Encoding with Error Handling (backslashreplace)
# Encode the string using ASCII and replace non-ASCII characters with backslash escape sequences.
string_5 = "Pythön"
encoded_backslash = string_5.encode("ascii", errors="backslashreplace")
print(encoded_backslash)  # Expected output: b'Pyth\\xf6n'
