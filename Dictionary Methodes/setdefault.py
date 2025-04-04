Dictionary1 = {'A': 'python ', 'B': 'class'}
print("Dictionary before using setdefault():", Dictionary1)

# using setdefault() when key is non-existing
ret_value = Dictionary1.setdefault('C', "Electro")
print("Return value of setdefault():", ret_value)

print("Dictionary after using setdefault():", Dictionary1)
