list1 = input().strip().split(',')
list2 = input().strip().split(',')
combined_list = []

for pos in range(len(list1)):
    combined_list.append(list1[pos])
    combined_list.append(list2[pos])

print(','.join(combined_list))