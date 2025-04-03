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

get() Method
Python Dictionary get() Method returns the value for the given key if present in the dictionary. If not, then it will return None (if get() is used with only one argument).

- get() Method Syntax:
  Syntax : Dict.get(key, Value)
- Parameters:
  key: The key name of the item you want to return the value from
  Value: (Optional) Value to be returned if the key is not found. The default value is None.
- Returns:
  Returns the value of the item with the specified key or the default value.

items() method
items() method in Python returns a view object that contains all the key-value pairs in a dictionary as tuples. This view object updates dynamically if the dictionary is modified.
-items() syntax
dict.items()
Here, dict is the dictionary from which the key-value pairs are retrieved.

- parameters
  items() method does not take any parameters.
- Return value:
  This method returns a dict_items view object, which behaves like a list of (key, value) tuples. If the dictionary is updated, the view object automatically reflects these changes.

keys() method
keys() method in Python returns a view object displaying all the dictionary’s keys. This view reflects changes made to the dictionary, meaning it updates automatically when the dictionary is modified.

- keys() syntax
  dict.keys()
  Here, dict is the dictionary from which the keys are to be returned.
- Parameters:
  None: keys() method does not take any parameters.
- Returns:
  A view object that displays a list of all the keys in the dictionary. This object is dynamic, meaning that if the dictionary is modified, the view object will reflect those changes.
