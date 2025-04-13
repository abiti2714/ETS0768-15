# Example 1
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.update(set2)
print(set1)
# Example 2
set3 = {1, 2, 3}
set3.update([4, 5, 6])

print(set3)
# Example 3
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {1, 2}

d2.update(d1.keys())
print(d2)
