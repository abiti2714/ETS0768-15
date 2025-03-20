-definition:

- String upper () Method

upper() method in Python is a built-in string method that converts all lowercase letters in a string to uppercase. This method is simple to use and does not modify the original string; instead, it returns a new string with the modifications applied.
-Syntax of upper() method :- string.upper()
-Parameters :- The upper() method does not take any parameters.
-Return Type :- This method returns a new string in which all lowercase characters in the original
string are converted to uppercase. If the original string has no lowercase letters then it returns the string unchanged.

- String lower() Method

The lower() method in Python converts all uppercase letters in a string to their lowercase. This method does not alter non-letter characters (e.g., numbers, git initpunctuation).

- Syntax of lower() method :- string.lower()
- Parameters :- This method does not take any parameters.
- Return Type :- The lower() method returns a new string with all uppercase characters converted  
   to lowercase. The original string remains unchanged since strings in Python are immutable.
- Practical applications of lower() :- The lower() method is very useful in various scenarios, such
  as making case-insensitive comparisons between strings.

  - String Title method

  title() method in Python is a simple way to convert a string to a title case, where the first letter of each word is capitalized and all other letters are lowercase.

- Syntax of String title() :- string.title()
- Parameters z:- title() doesn’t accept any parameter.
- Return type :- string, converted to title case.

- String capitalize() Method

The capitalize() method in Python is used to change the first letter of a string to uppercase and make all other letters lowercase. It is especially useful when we want to ensure that text follows title-like capitalization, where only the first letter is capitalized.

- Syntax of capitalize() Method :- s.capitalize()
- Parameters :-The capitalize() method does not accept any parameters.
- Return Value :- The method returns a new string with the first character capitalized and all other characters in lowercase. The original string remains unchanged.

- String casefold() Method

Python String casefold() method is used to convert string to lowercase. It is similar to the Python lower() string method, but the case removes all the case distinctions present in a string.

- Syntax: string.casefold()
- Parameters: The casefold() method doesn’t take any parameters.
- Return value: Returns the case folded string the string converted to lower case.

- String center() Method

  center() method in Python is a simple and efficient way to center-align strings within a given width. By default, it uses spaces to fill the extra space but can also be customized to use any character we want.

- Syntax :- string.center(length[, fillchar])
- Parameters:-
  length: length of the string after padding with the characters.
  fillchar: (optional) characters which need to be padded. If it’s not provided, space is taken as the default argument.
- Returns:-
  Returns a string padded with specified fillchar and it doesn’t modify the original string.
