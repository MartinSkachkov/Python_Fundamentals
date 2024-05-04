target = int(input())
lst = [int(el) for el in input().split(' ')]

l = 0
r = len(lst) - 1
lst.sort()

while l < r:
    curr_sum = lst[l] + lst[r]

    if curr_sum < target:
        l += 1
    elif curr_sum > target:
        r -= 1
    else:
        print(f'({lst[l]},{lst[r]})')
        l += 1
        r -= 1
