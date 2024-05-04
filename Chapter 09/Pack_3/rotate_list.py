lst = input().split(',')
n = int(input())

if n > len(lst):
    n %= len(lst)

for i in range(n):
    lst = lst[1:] + [lst[0]]

print(','.join(lst))