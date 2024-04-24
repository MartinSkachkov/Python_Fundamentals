row = 6  # int(input())
col = 3  # int(input())

for r in range(row):
    for c in range(col):
        print('*', end=' ')
    print()
#########################################################
# outer loop
for i in range(1, 11):
    # nested loop
    # to iterate from 1 to 10
    for j in range(1, 11):
        # print multiplication
        print(i * j, end=' ')
    print()
#########################################################
rows = 6
for r in range(rows):
    for i in range(r):
        print('*', end=' ')
    print()
#########################################################
names = ['Kelly', 'Jessa', 'Emma']
# outer loop
for name in names:
    # inner while loop
    count = 0
    while count < 5:
        print(name, end=' ')
        # increment counter
        count = count + 1
    print()
#########################################################
for i in range(4):
    for j in range(4):
        if j == i:
            break
        print(i, j)
# 1 0
# 2 0
# 2 1
# 3 0
# 3 1
# 3 2
#########################################################
first = [2, 4, 6]
second = [2, 4, 6]
for i in first:
    for j in second:
        if i == j:
            continue
        print(i, '*', j, '= ', i * j)
# 2 * 4 =  8
# 2 * 6 =  12
# 4 * 2 =  8
# 4 * 6 =  24
# 6 * 2 =  12
# 6 * 4 =  24
#########################################################
first = [2, 3, 4]
second = [20, 30, 40]
final = []
for i in first:
    for j in second:
        final.append(i+j)
print(final)
# [22, 32, 42, 23, 33, 43, 24, 34, 44]

first = [2, 3, 4]
second = [20, 30, 40]
final = [i+j for i in first for j in second]
print(final)
#########################################################
final = [[x, y] for x in [10, 20, 30] for y in [30, 10, 50] if x != y]
print(final)
# [[10, 30], [10, 50], [20, 30], [20, 10], [20, 50], [30, 10], [30, 50]]
#########################################################
print('Show Perfect number from 1 to 100')
n = 2
# outer while loop
while n <= 100:
    x_sum = 0
    # inner for loop
    for i in range(1, n):
        if n % i == 0:
            x_sum += i
    if x_sum == n:
        print('Perfect number:', n)
    n += 1
#########################################################
numbers = [[1, 2, 3], [4, 5, 6]]

cnt = 0
for i in numbers:
    for j in i:
        print('iteration', cnt, end=': ')
        print(j)
        cnt = cnt + 1
# iteration 0: 1
# iteration 1: 2
# iteration 2: 3
# iteration 3: 4
# iteration 4: 5
# iteration 5: 6
