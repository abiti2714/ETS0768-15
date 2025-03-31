# Example 1
My_list1 = [1, 2, 3, 4, 5, 6, 7, 8]

# List of elements to remove
My_list_2 = [2, 4, 6]

# Remove elements from main_list that are in remove_list
for item in My_list_2:
    if item in My_list1:
        My_list1.remove(item)

print(My_list1)


# Example 2

My_list4 = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

My_list4.remove([1, 2])
print(My_list4)
