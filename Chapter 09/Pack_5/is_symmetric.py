def is_symmetric(lst):
    i = 0
    steps = len(lst) // 2

    while i < steps:
        if lst[i] == lst[len(lst) - 1 - i]:
            i += 1
        else:
            return 'No'

    return 'Yes'


n = int(input())

results = []

for _ in range(n):
    arr = input().split(' ')
    results.append(is_symmetric(arr))
    arr.clear()

for res in results:
    print(res)
