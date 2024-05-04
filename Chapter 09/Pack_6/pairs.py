target = int(input())
lst = [int(el) for el in input().split(' ')]

found_pair = False

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == target:
            found_pair = True
            print(f'{lst[i]},{lst[j]}')

if not found_pair:
    print('no pairs')
