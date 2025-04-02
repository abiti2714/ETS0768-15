sequence = {'a', 'b', 'c', 'd', 'e'}

# creating dict with default values as None
res_dict = dict.fromkeys(sequence)

print("The newly created dict with None values : " + str(res_dict))

# creating dict with default values as 1
res_dict2 = dict.fromkeys(sequence, 1)

print("The newly created dict with 1 as value : " + str(res_dict2))
