-definition:

- String upper () Method

upper() method in Python is a built-in string method that converts all lowercase letters in a string to uppercase. This method is simple to use and does not modify the original string; instead, it returns a new string with the modifications applied.
-Syntax of upper() method :-
string.upper()
-Parameters :-
The upper() method does not take any parameters.
-Return Type :-
This method returns a new string in which all lowercase characters in the original
string are converted to uppercase. If the original string has no lowercase letters then it returns the string unchanged.

- String lower() Method

The lower() method in Python converts all uppercase letters in a string to their lowercase. This method does not alter non-letter characters (e.g., numbers, git initpunctuation).

- Syntax of lower() method :-
  string.lower()
- Parameters :-
  This method does not take any parameters.
- Return Type :-
  The lower() method returns a new string with all uppercase characters converted  
   to lowercase. The original string remains unchanged since strings in Python are immutable.
- Practical applications of lower() :-
  The lower() method is very useful in various scenarios, such
  as making case-insensitive comparisons between strings.

- String Title method

  title() method in Python is a simple way to convert a string to a title case, where the first letter of each word is capitalized and all other letters are lowercase.

- Syntax of String title() :-
  string.title()
- Parameters z:-
  title() doesn’t accept any parameter.
- Return type :-
  string, converted to title case.

- String capitalize() Method

The capitalize() method in Python is used to change the first letter of a string to uppercase and make all other letters lowercase. It is especially useful when we want to ensure that text follows title-like capitalization, where only the first letter is capitalized.

- Syntax of capitalize() Method :-
  s.capitalize()
- Parameters :-
  The capitalize() method does not accept any parameters.
- Return Value :-
  The method returns a new string with the first character capitalized and all other characters in lowercase. The original string remains unchanged.

- String casefold() Method

Python String casefold() method is used to convert string to lowercase. It is similar to the Python lower() string method, but the case removes all the case distinctions present in a string.

- Syntax:
  string.casefold()
- Parameters:
  The casefold() method doesn’t take any parameters.
- Return value:
  Returns the case folded string the string converted to lower case.

- String center() Method

  center() method in Python is a simple and efficient way to center-align strings within a given width. By default, it uses spaces to fill the extra space but can also be customized to use any character we want.

- Syntax :-
  string.center(length[, fillchar])
- Parameters:-
  length: length of the string after padding with the characters.
  fillchar: (optional) characters which need to be padded. If it’s not provided, space is taken as the default argument.
- Returns:-
  Returns a string padded with specified fillchar and it doesn’t modify the original string.

- String count() Method

  The count() method in Python returns the number of times a specified substring appears in a string. It is commonly used in string analysis to quickly check how often certain characters or words appear.

- Syntax of count() Method :-
  string.count(substring, start = 0, end = len(s))
- Parameters :-
  substring (required): The substring we want to count within the original string.
  start (optional): The index position in the string where the search should begin. Default is 0.
  end (optional): The index position in the string where the search should stop. Default is the length of the string (i.e., up to the end).
- Return Type :-
  The count() method returns an integer representing the number of times the specified substring appears within the given range of the string.

Strings encode() method

String encode() method in Python is used to convert a string into bytes using a specified encoding format. This method is beneficial when working with data that needs to be stored or transmitted in a specific encoding format, such as UTF-8, ASCII, or others.
-Syntax of encode() method
string.encode(encoding=”utf-8″, errors=”strict”)
-Parameters
encoding (optional):
The encoding format to use. The default is "utf-8".
Examples include "ascii", "latin-1", "utf-16", etc.
-Return Type
Returns a bytes object containing the encoded version of the string.

- String endswith() Method

  The endswith() method is a tool in Python for checking if a string ends with a particular substring. It can handle simple checks, multiple possible endings and specific ranges within the string. This method helps us make our code cleaner and more efficient, whether we’re checking for file extensions, validating URLs or processing text.
  -Syntax of endswith() Method:
  str.endswith(suffix, start, end)
  -Parameters:
  suffix: Suffix is nothing but a string that needs to be checked.
  start: Starting position from where suffix is needed to be checked within the string.
  end: Ending position + 1 from where suffix is needed to be checked within the string.
  -Return:
  Returns True if the string ends with the given suffix otherwise return False.

expandtabs() method

expandtabs() method in Python is used to replace all tab characters (\t) in a string with spaces. This method allows for customizable spacing, as we can specify the number of spaces for each tab. It is especially useful when formatting text for better readability or alignment.
-Syntax of expandtabs() method:-
string.expandtabs(tabsize)
-Parameters:-
tabsize (optional) : Specifies the number of spaces per tab. The default value is 8.

- Return Type:-
  This method returns a new string with all the tab characters replaced with spaces.

find() Method

The find() method in Python returns the index of the first occurrence of a substring within a given string. If the substring is not found, it returns -1. This method is case-sensitive, which means “abc” is treated differently from “ABC“.
-Syntax of find() Method:-
s.find(substring, start, end)

- Parameter:-
  ubstring: The substring to search for within the main string s.
  start (optional): The starting index from where to begin the search.
  end (optional): The ending index where the search should stop.
  -Return Value:-
  Returns the first index of the substring if it is found within the specified range.
  Returns -1 if the substring is not found.

  format() Method

The format() method is a powerful tool that allows developers to create formatted strings by embedding variables and values into placeholders within a template string. This method offers a flexible and versatile way to construct textual output for a wide range of applications. Python string format() function has been introduced for handling complex string formatting more efficiently. Sometimes we want to make generalized print statements in that case instead of writing print statements every time we use the concept of formatting.
-Syntax: { }.format(value)
-Parameters:
value : Can be an integer, floating point numeric constant, string, characters or even variables.
-Returntype:-
Returns a formatted string with the value passed as parameter in the placeholder position.

String format_map() Method

Python String format_map() method is an inbuilt function in Python, which is used to return a dictionary key’s value.

- Syntax:-
  string.format_map(z)
- Parameters :-
  Here z is a variable in which the input dictionary is stored and string is the key of the input dictionary. input_dict: Takes a single parameter which is the input dictionary.
- Returns:-
  Returns key’s values of the input dictionary.

String index() Method

The index() method in Python is used to find the position of a specified substring within a given string. It is similar to the find() method but raises a ValueError if the substring is not found, while find() returns -1. This can be helpful when we want to ensure that the substring exists in the string before proceeding.

- Syntax of index() :-
  s.index(substring, start=0, end=len(s))
- Parameters:-
  substring: The substring to locate within the string s.
  start (optional): The starting index for the search. Defaults to 0 if not provided.
  end (optional): The ending index for the search. If not provided, it defaults to the length of the string.
- Return Type:-
  Returns the lowest index of the substring if found in the given string.
  Raises a ValueError if the substring is not found in the specified range.

String isdigit() Method

The isdigit() method is a built-in Python function that checks if all characters in a string are digits. This method returns True if each character in the string is a numeric digit (0-9), and False otherwise.

- Syntax of isdigit() :-
  s.isdigit()
- Parameters:-
  The isdigit() metho~d does not take any parameters
- Return Value:-
  Returns True if all characters in the string are numeric (0-9).
  Returns False if there are any non-numeric characters.

swapcase() Method

swapcase() method in Python is used to return a new string where all the uppercase characters in the original string are converted to lowercase, and all the lowercase characters are converted to uppercase.
-Syntax of String swapcase() method:-
string.swapcase()

- Parameters:-
  The swapcase() method does not take any parameters.
- Return Type:-
  Returns a new string where all uppercase characters are converted to lowercase and all lowercase characters are converted to uppercase.

strip() Method

strip() method removes all leading and trailing whitespace characters from a string in Python. We can also customize it to strip specific characters by passing a string of characters to remove. It doesn’t modify the original string but returns a new one.
-Syntax of strip() Method:-
s.strip(chars)
-Parameters::-
chars(optional)A string specifying the set of characters to remove from the beginning and end of the string.
If omitted, strip() removes all leading and trailing whitespace by default.
-Return Type::-
String: A new string with the specified characters (or whitespace) removed from both ends is returned.

lstrip() Method

The lstrip() method removes leading whitespace characters from a string. We can also specify custom characters to remove from the beginning/starting of the string.
-Syntax of lstrip() Method:-
s.lstrip(chars)
s: The input string
chars (optional): A set of characters to remove as trailing characters

String rstrip() Method
The rstrip() method removes trailing whitespace characters from a string. We can also specify custom characters to remove from end of string.

- Syntax of rstrip() Method
  s.rstrip(chars)
  s: The input string
  chars (optional): A set of characters to remove as trailing characters

String replace() Method

The replace() method replaces all occurrences of a specified substring in a string and returns a new string without modifying the original string

- Syntax of String replace() Method
  string.replace(old, new, count)
- Parameters
  old: The substring we want to replace.
  new: The new substring that we want to replace with old substring.
  count (optional): Specifies the maximum number of replacements to perform. If omitted, all occurrences are replaced.
- Return Type
  Returns a new string with the specified replacements made. The original string remains unchanged since strings in Python are immutable.

Python String rsplit() Method
Python String rsplit() method returns a list of strings after breaking the given string from the right side by the specified separator. It’s similar to the split() method in Python, but the difference is that rsplit() starts splitting from the end of the string rather than from the beginning.

- Syntax of rsplit() method
  str.rsplit(separator, maxsplit)
- Parameters
  separator: The is a delimiter. The string splits at this specified separator starting from the right side. If not provided then any white space character is a separator.
  maxsplit: It is a number, which tells us to split the string into a maximum of provided number of times. If it is not provided then there is no limit.  
  -Return Type
  Returns a list of strings after breaking the given string from the right side by the specified separator.
- Error: We will not get any error even if we are not passing any argument.

String join() Method
The join() method in Python is used to concatenate the elements of an iterable (such as a list, tuple, or set) into a single string with a specified delimiter placed between each element.
-Syntax of join()
separator.join(iterable)

- Parameters:
  separator: The string placed between elements of the iterable.
  iterable: A sequence of strings (e.g., list, tuple etc) to join together.
- Return Value:
  Returns a single string formed by joining all elements in the iterable, separated by the specified separator
  If the iterable contains any non-string values and it raises a TypeError exception.

String startswith()

startswith() method in Python is a built-in string method that checks whether a given string starts with a specific prefix. It helps in efficiently verifying whether a string begins with a certain substring, which can be useful in various scenarios like filtering or validating input. In this article, we will understand about startswith() method.
-Syntax of startswith() method
string.startswith(prefix[, start[, end]])

- Parameters:
  prefix: The substring or a tuple of substrings to check for at the start of the string.
  start (optional): The index where the search for the prefix begins. By default, it starts from index 0.
  end (optional): The index where the search for the prefix ends. If not specified, the search goes till the end of the string.
  -Return Type:
  The method returns a Boolean:
  True if the string starts with the specified prefix.
  False if it does not.

String isalpha() Method

The isalpha() method checks if all characters in a given string are alphabetic. It returns True if every character in the string is a letter and False if the string contains any numbers, spaces, or special characters.

- Syntax of isalpha() Method
  string.isalpha()
- Parameter:
  No parameters are required.
- Return Type:
  Returns True if all characters in string are alphabetic (A-Z, a-z) and False otherwise.

String translate() Method

Python translate() method is used to transform a string by replacing or removing specific characters based on a translation table. This table is created using the str.maketrans() method. It’s ideal for scenarios where we need to:
Replace specific characters with others.
Remove unwanted characters like punctuation, digits or whitespace.
Perform transformations without looping through the string manually.
Syntax of translate() method:
str.translate(table)

- Parameters:
  table: A translation table created using the str.maketrans() method.
- Returns:
  A new string where the specified characters are replaced or removed according to the translation table.
- Python maketrans()
  The maketrans() method is a built-in string method in Python that generates a translation table. It is primarily used in conjunction with the translate() method to perform character-by-character translations or deletions.
- Python maketrans() Syntax
- Syntax: maketrans(str1, str2, str3)
- Parameters:
  str1: Specifies the list of characters that need to be replaced.
  str2: Specifies the list of characters with which the characters need to be replaced.
  str3: Specifies the list of characters that need to be deleted.
  -Returns:
  Returns the translation table which specifies the conversions that can be used by translate()

rjust() string methode

The string rjust() method returns a new string of given length after substituting a given character in left side of original string.

- Syntax:
  string.rjust(length, fillchar)
- Parameters:
- length: length of the modified string. If length is less than or equal to the length of the original string then original string is returned.
  -fillchar: (optional) characters which needs to be padded. If it’s not provided, space is taken as a default argument.
- Returns:
  Returns a new string of given length after substituting a given character in left side of original string.

String zfill()

zfill() method in Python is used to pad a string with zeros (0) on the left until it reaches a specified width.

- Syntax of zfill() method
  string.zfill(width)
- Parameters
  width (required):
  The total length of the string after padding.
  If the specified width is less than or equal to the length of the original string, no padding is applied.
- Return Type
  Returns a new string with zeros padded on the left to meet the specified width.
