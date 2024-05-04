lst = input().split(', ')
lst_num = []

for elem in lst:
    lst_num.append(int(elem))

lst_num.sort(reverse=True)

lst.clear()
for elem in lst_num:
    lst.append(str(elem))

print(', '.join(lst))