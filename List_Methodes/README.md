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
