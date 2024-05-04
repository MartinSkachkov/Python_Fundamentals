array = input().split(',')
n = len(array)

not_in_arr = []

for i in range(1, n+1):
    if str(i) in array:
        continue
    else:
        not_in_arr.append(str(i))


print(','.join(not_in_arr))