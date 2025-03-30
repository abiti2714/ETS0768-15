- List.append() Method
  append() method in Python is used to add a single item to the end of list. This method modifies the original list and does not return a new list. Let’s look at an example to better understand this.
- Syntax of append() method
  list.append(element)
- Parameter:
  element: The item to be appended to the list. This can be of any data type (integer, string, list, object, etc.). This parameter is mandatory, and omitting it will cause an error.
- Return:
  append() does not return any value. It modifies the original list in place.

Deep copy

A deep copy creates a new compound object before inserting copies of the items found in the original into it in a recursive manner.
It will first construct a new collection object and then recursively populate it with copies of the child objects found in the original. It means that any changes made to a copy of the object do not reflect in the original object.

- Syntax of Python Deepcopy
  copy.deepcopy()

Shallow copy

A shallow copy creates a new object but retains references to the objects contained within the original. It only copies the top-level structure without duplicating nested elements.
Changes made to a copy of an object do reflect in the original object. In python, this is implemented using the “copy.copy()” function.

- Syntax of Python Shallowcopy
  copy.copy()

List clear() Method

clear() method in Python is used to remove all elements from a list, effectively making it an empty list. This method does not delete the list itself but clears its content. It is a simple and efficient way to reset a list without reassigning it to a new empty list.
-Syntax of clear() Method
list.clear()

- Parameters:
  The clear() method does not take any parameters.
- Return Type:
  It modifies the original list and does not return any value (None).

List count() method

The count() method is used to find the number of times a specific element occurs in a list. It is very useful in scenarios where we need to perform frequency analysis on the data.

- Syntax of count() Method
  list_name.count(value)
  list_name: The list object where we want to count an element.
- value: The element whose occurrences need to be counted.
  The count() method returns an integer value, which represents the number of times the specified element appears in the list

List extend() Method

In Python, extend() method is used to add items from one list to the end of another list. This method modifies the original list by appending all items from the given iterable.
Using extend() method is easy and efficient way to merge two lists or add multiple elements at once.

- Syntax of List extend() Method
  list_name.extend(iterable)
- Parameters:
  list_name: The list that will be extended
  iterable: Any iterable (list, set, tuple, etc.)
- Returns:
  Python List extend() returns none.

List index() – Find Index of Item

list index() method searches for a given element from the start of the list and returns the position of the first occurrence.

- Syntax of List index() Method
  Syntax: list_name.index(element, start, end)
- Parameters:
  element: The element whose lowest index will be returned.
  start(optional): The position from where the search begins.
  end(optional): The position from where the search ends.
