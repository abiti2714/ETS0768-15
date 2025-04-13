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

symmetric_difference_update()
The symmetric difference between the two sets is the set of elements that are in either of the sets but not in both of them.
symmetric_difference() method returns a new set that contains a symmetric difference of two sets. The symmetric_difference_update() method updates the set by calling symmetric_difference_update() with the symmetric difference of sets.

- symmetric_difference_update() Syntax
- Syntax: A.symmetric_difference_update(B)
- Parameters:
  The symmetric_difference takes a single “iterable” as an argument. Iterable should contain hashable object.
- Returns:
  This method returns None (which indicates absence of a return value). It only updates the set calling symmetric_difference_update() with the symmetric difference of sets.

Union() function
Union() method in Python is an inbuilt function provided by the set data type. It is used to combine multiple sets into a single set, containing all unique elements from the given sets. It ensures that no duplicate values exist in the final set.

- Union() Syntax
  set1.union(set2, set3, …)
- Parameters:
  Zero or more sets can be passed as arguments.
  If no parameter is provided, a copy of set1 is returned.
- Returns:
  A new set containing the union of all given sets.
  Ensures no duplicate elements in the final set.

Python Set update()
The update() method in Python is used to modify dictionaries and sets. For dictionaries, it merges key-value pairs from another dictionary, iterable, or keyword arguments, updating existing keys or adding new ones. For sets, it adds elements from iterables (like lists or tuples), ignoring duplicates. For example, dict1.update(dict2) merges dictionaries, while set1.update([3, 4, 5]) adds elements to a set. It modifies the original collection in place, making it efficient for combining or updating data.

- Syntax of set update():
  dict.update([other])
  other: This can be another dictionary, an iterable of key-value pairs (like a list of tuples), or keyword arguments.
  If a key already exists in the dictionary, its value is updated. If the key does not exist, it is added to the dictionary.

- update() method for dictionaries
  update() method for dictionaries is used to add or update key-value pairs from one dictionary (or an iterable of key-value pairs) into another dictionary.
- Update() method for set
  The update() method for sets is used to add elements from another set, list, tuple, or any iterable to the set. It is used to add elements from one or more iterables (like sets, lists, tuples, etc.) to an existing set. When we call set1.update(iterable), the elements from the iterable are added to set1. Since sets only store unique elements, any duplicates in the iterable are automatically ignored.
- Syntax:
  set.update(*others)
  *others: This can be one or more iterables (like sets, lists, tuples, etc.).
  Duplicate elements are ignored because sets only store unique elements.
- Adding Elements of a Dictionary to a Set
  If we want to add the keys or values of a dictionary to a set, we can use the update() method in combination with dictionary methods like .keys() or .values().
