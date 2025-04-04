# working of pop()

# initializing dictionary
test_dict = {"Name": 'Kibrom',
             "field of study": 'Engineering', "department": 'Electro'}

# Printing initial dict
print("The dictionary before deletion : " + str(test_dict))

# using pop to return and remove key-value pair.
pop_ele = test_dict.pop('field of study')

# Printing the value associated to popped key
print("Value associated to popped key is : " + str(pop_ele))

# Printing dictionary after deletion
print("Dictionary after deletion is : " + str(test_dict))
