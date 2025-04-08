Set add() Method in Python
The set.add() method in Python adds a new element to a set while ensuring uniqueness. It prevents duplicates automatically and only allows immutable types like numbers, strings, or tuples. If the element already exists, the set remains unchanged, while mutable types like lists or dictionaries cannot be added due to their unhashable nature.

- Set add() Syntax
  set.add( elem )
  -Parameter:
  elem is the element to be added to the set.
- Returns:
  It does not return anything (None).

- Set clear() Method
  Python Set clear() method removes all elements from the set.
- Python Set clear() Method Syntax:
  Syntax: set.clear()
- parameters:
  The clear() method doesn’t take any parameters.
- Return: None

- set copy() in python
  The copy() method returns a shallow copy of the set in python. If we use “=” to copy a set to another set, when we modify in the copied set, the changes are also reflected in the original set. So we have to create a shallow copy of the set such that when we modify something in the copied set, changes are not reflected back in the original set.
- Syntax:
  set_name.copy()
  set_name: Name of the set whose copy we want to generate.
- Parameters:
  The copy() method for sets doesn’t take any parameters. Return value:The function returns a shallow copy of the original set.
