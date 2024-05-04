# 0,1,0,3,12 -> 1,3,12,0,0

lst = [int(el) for el in input().split(',')]

count_zeroes = 0
for el in lst:
    if el == 0:
        count_zeroes += 1

for _ in range(count_zeroes):
    lst.remove(0)  # removing the first zeroes
    lst.append(0)  # then appending them to the back

print(','.join([str(el) for el in lst]))
