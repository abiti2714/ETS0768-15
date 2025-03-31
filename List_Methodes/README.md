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

insert() Method With Examples
Python List insert() method inserts an item at a specific index in a list.
List insert() method in Python is very useful to insert an element in a list. What makes it different from append() is that the list insert() function can add the value at any position in a list, whereas the append function is limited to adding values at the end.
It is used in editing lists with huge amount of data, as inserting any missed value in that list is made very easy with this Python function.

- List insert() Method Syntax
  list_name.insert(index, element)
- Parameters:
  index: the index at which the element has to be inserted.
  element: the element to be inserted in the list.
- Return : The insert() method returns None. It only updates the current list.

List pop() Method
The pop() method is used to remove an element from a list at a specified index and return that element. If no index is provided, it will remove and return the last element by default. This method is particularly useful when we need to manipulate a list dynamically, as it directly modifies the original list.
-Syntax of pop() method
list_name.pop(index)

- Parameters
  index (optional): index of an item to remove. Defaults to -1 (last item) if argument is not provided.
- Return Value
  Returns the removed item from the specified index
  Raises IndexError if the index is out of range.

remove() Method
Python list remove() function removes the first occurrence of a given item from list. It make changes to the current list. It only takes one argument, element we want to remove and if that element is not present in the list, it gives ValueError.

- Syntax of remove() method
  list_name.remove(obj)
- Parameter
  obj: object to be removed from the list
- Return Type
  The method does not return any value but removes the given object from the list.
  Exception: If the element doesn’t exist, it throws ValueError: list.remove(x): x not in list exception.
