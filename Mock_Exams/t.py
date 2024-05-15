from copy import deepcopy

l = (1, 2, 3, 4, 5, 5)
l2 = deepcopy(l)

print(l2 is l)
print(l)