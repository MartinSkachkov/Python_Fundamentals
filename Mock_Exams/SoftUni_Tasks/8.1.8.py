n = int(input())

lst = []

for _ in range(n):
    lst.append(int(input()))

max = 0
curr_seq = 1
updated_max = False

for i in range(1, len(lst)):
    if lst[i-1] < lst[i]:
        curr_seq += 1
    else:
        if curr_seq > max:
            max = curr_seq
            updated_max = True
        curr_seq = 1

if not updated_max:
    max = curr_seq

print(max)
