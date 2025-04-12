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

  Intersection() Methode
  Python set intersection() method returns a new set with an element that is common to all set

The intersection of two given sets is the largest set, which contains all the elements that are common to both sets. The intersection of two given sets A and B is a set which consists of all the elements which are common to both A and B.

- Syntax:
  set1.intersection(set2, set3, set4….)
- Parameters:
  any number of sets can be passed
- Return:
  Returns a set which has the intersection of all sets(set1, set2, set3…) with set1. It returns a copy of set1 only if no parameter is passed.

Set isdisjoint() Method
Python set isdisjoint() function check whether the two sets are disjoint or not, if it is disjoint then it returns True otherwise it will return False. Two sets are said to be disjoint when their intersection is null.

- Python set isdisjoint() Method Syntax:
  Syntax: set1.isdisjoint(set2)
- Parameters:
  another set to compare with or an iterable (list, tuple, dictionary, and string)
  Return: bool

Set issubset() Method
Python set issubset() method returns True if all elements of a set A are present in another set B which is passed as an argument, and returns False if all elements are not present in Python.

- Python Set issubset() Method Syntax
  Syntax: set_obj.issubset(other_set)
- Parameter:
  other_set: any other set to compare with.
- Return: bool

issuperset() in Python
Python Set issuperset() method returns True if all elements of a set B are in set A. Then Set A is the superset of set B.
Python issuperset() Method Syntax:
-Syntax: A.issuperset(B)

- Parameter: Any other Set to compare with
- Return: boolean value

Python Set pop() Method
Python set pop() removes any random element from the set and returns the removed element.

- Set pop() Syntax
  Syntax: set_obj.pop()
- Parameter: set.pop() doesn’t take any parameter.
- Return: Returns the popped element from the set

symmetric_difference()
The symmetric difference of two sets set1 and set2 is the set of elements which are in either of the sets set1 or set2 but not in both.

- Syntax :
  set1_name.symmetric_difference(set2_name)
- Parameters :
  It only takes a single set as the parameter. If a list, tuple or dictionary is passed it converts it a set and performs the task.
- Return value :
  Returns a set which is the symmetric difference between the two sets.
