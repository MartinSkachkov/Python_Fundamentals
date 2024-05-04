n = int(input())
l1 = []
l2 = []

for i in range(n):
    l1.append(int(input()))

for i in range(n):
    l2.append(int(input()))

if l1 == l2:
    print('equal')
else:
    print('not equal')
