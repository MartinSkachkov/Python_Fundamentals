from copy import deepcopy
s = 'FfEeDdCcBbAa'
s = s[::-1]

upper = s[1::2]
lower = s[::2]

print(upper, lower)

###########################
t1 = 1, 2, 3, 4, 5, 6
t2 = 7, 8, 9, 10
t3 = 11, 12, 13, 14, 15, 16, 17

l1 = list(t1)
l2 = list(t2)
l3 = list(t3)

l1[::2] = len(l1[::2]) * [0]
l2[::2] = len(l2[::2]) * [0]
l3[::2] = len(l3[::2]) * [0]

merged = tuple(l1 + l2 + l3)

print(merged)

###########################
m = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for row in range(len(m)):
    for col in range(len(m[row])):
        if row == col:
            m[row][col] = 1

print(m)

###########################

m1 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

m1_copy = deepcopy(m1)

for row in range(len(m)):
    for col in range(len(m[row])):
        if row == col:
            m1_copy[row][col] = 1

print(m1)
print(m1_copy)

###########################
data = [
    (100, 'USD', 'EUR', 0.83),
    (100, 'USD', 'CAD', 1.27),
    (100, 'CAD', 'EUR', 0.65)
]

for elem in data:
    print(f'{elem[0]} {elem[1]} = {(elem[0] * elem[3]):.2f} {elem[2]}')

###########################
l1 = [1, 2, 3, 1, 5, 1, 9, 4, 1, 3]
i = 0

while i < len(l1):
    print(len(l1))
    if l1[i] == 1:
        del l1[i]
    else:
        i += 1
