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

pop() Method
Python dictionary pop() method removes and returns the specified element from the dictionary.
Dictionary pop() function in Python is an in-built function that is used to remove and return an element from a dictionary. It can take one or two arguments.
Dictionary pop() function is very useful in the conditional removal of elements and handling missing values. It not only allows us to remove an element but we can also access its value.

- Syntax of Dictionary pop()
  dict.pop(key, def)
- Parameters :
  key : The key whose key-value pair has to be returned and removed.
  def : The default value to return if specified key is not present.
- Returns :
  The value associated with the deleted key-value pair, if the key is present.
  Default value if specified if key is not present.
  KeyError, if key not present and default value not specified.

popitem() method
popitem() method in Python is used to remove and return the last key-value pair from the dictionary. It is often used when we want to remove a random element, particularly when the dictionary is not ordered.

- popitem() syntax
  dict.popitem()
  Here, dict is the dictionary from which the key-value pair is to be removed.
- Parameter:
  None: The popitem() method does not take any parameters.
- Returns:
  This method returns a tuple containing the last key-value pair removed from the dictionary.
  If the dictionary is empty, it raises a KeyError.

setdefault() Method
Python Dictionary setdefault() returns the value of a key (if the key is in dictionary). Else, it inserts a key with the default value to the dictionary.

- setdefault() Method Syntax:
  Syntax: dict.setdefault(key, default_value)
- Parameters:
  It takes two parameters:
  key – Key to be searched in the dictionary.
  default_value (optional) – Key with a value default_value is inserted to the dictionary if key is not in the dictionary. If not provided, the default_value will be None.
- Returns:
  Value of the key if it is in the dictionary.
  None if key is not in the dictionary and default_value is not specified.
  default_value if key is not in the dictionary and default_value is specified.

  values() methode
  values() method in Python is used to obtain a view object that contains all the values in a dictionary. This view object is dynamic, meaning it updates automatically if the dictionary is modified.. If we use the type() method on the return value, we get “dict_values object”. It must be cast to obtain the actual list.

- values() syntax
  dict.values()
  Here, dict is the dictionary from which the values are to be retrieved.
  -Parameters:
  values() method does not take any parameters.
- Returns:
  This method returns a dict_values view object, which behaves like a dynamic list of all the values in the dictionary. If the dictionary is updated, the view reflects these changes automatically.

update() method
Python Dictionary update() method updates the dictionary with the elements from another dictionary object or from an iterable of key/value pairs.
Syntax of Dictionary update Method
The dictionary update() method in Python has the following syntax:

- Syntax:
  dict.update([other])
- Parameters:
  This method takes either a dictionary or an iterable object of key/value pairs (generally tuples) as parameters.
- Returns:
  It doesn’t return any value but updates the Dictionary with elements from a dictionary object or an iterable object of key/value pairs.
