def is_sorted(lst):
    res = True

    if len(lst) == 1:
        return res

    # list has at least two elements
    i = 1
    while i <= len(lst) - 1:
        if int(lst[i-1]) <= int(lst[i]):
            res = True
        else:
            res = False
            break

        i += 1

    return res


n = int(input())

results = []

for _ in range(n):
    lst = input().split(',')
    results.append(f'{is_sorted(lst)}')
    lst.clear()

for res in results:
    print(res.lower())
