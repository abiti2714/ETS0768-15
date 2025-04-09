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

  difference() Methode
  In Python, the difference() method is used to find elements that exist in one set but not in another. It returns a new set containing elements from the first set that are not present in the second set. This operation is similar to the subtraction of sets (A – B), where only unique elements from the first set remain.

- Syntax:
  set_A.difference(set_B) for (A – B)
  set_B.difference(set_A) for (B – A)

  difference_update()
  The difference_update() method helps in an in-place way of differentiating the set. The previously discussed set difference() helps to find out the difference between two sets and returns a new set with the difference value, but the difference_update() updates the existing caller set.
  If A and B are two sets. The set difference() method will get the (A – B) and will return a new set. The set difference_update() method modifies the existing set. If (A – B) is performed, then A gets modified into (A – B), and if (B – A) is performed, then B gets modified into (B – A).

- Syntax:
  A.difference_update(B) for (A - B)
  B.difference_update(A) for (B - A)
- return value:
  The function returns None and changes the value of the existing set.

frozenset() in Python
Python Method creates an immutable Set object from an iterable. It is a built-in Python function. As it is a set object, therefore, we cannot have duplicate values in the frozenset.

- frozenset() Syntax
  Syntax : frozenset(iterable_object_name)
- Parameter : iterable_object_name
  This function accepts iterable object as input parameter.
  Return : Returns an equivalent frozenset object.
