Dictionary clear()

clear() method in Python is used to remove all items (key-value pairs) from a dictionary. After calling this method, the dictionary will become empty and its length will be 0. This method is part of the built-in dictionary operations in Python.

- clear() syntax
  dict.clear()
  Here, dict is the dictionary on which the clear() method is called.
- Parameters:
  None: clear() method does not take any parameters.
- Returns:
  This method does not return anything. It modifies the dictionary in place, removing all items from it.

- Dictionary copy()

Python Dictionary copy() method returns a shallow copy of the dictionary.

- Syntax of copy() method
  Syntax: dict.copy()
- Return:  
  This method doesn’t modify the original, dictionary just returns copy of the dictionary.
- Python Dictionary copy() Error:
  As we are not passing any parameters, there is no chance of any error.

- Dictionary fromkeys() Method
  Python dictionary fromkeys() function returns the dictionary with key mapped and specific value. It creates a new dictionary from the given sequence with the specific value.
- fromkeys() Method Syntax:
  Syntax : fromkeys(seq, val)
  Parameters :
  seq : The sequence to be transformed into a dictionary.
  val : Initial values that need to be assigned to the generated keys. Defaults to None.
- Returns :
  A dictionary with keys mapped to None if no value is provided, else to the value provided in the field.
