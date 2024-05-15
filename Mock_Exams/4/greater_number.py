arr1 = [int(digit) for digit in input().split(',')]
arr2 = [int(digit) for digit in input().split(',')]

output = []

for elem in arr1:
    index = None
    flag = False

    for i in range(len(arr2)):
        if arr2[i] == elem:
            index = i
            break

    for i in range(index+1, len(arr2)):
        if arr2[i] > elem:
            output.append(str(arr2[i]))
            flag = True
            break

    if not flag:
        output.append('-1')

print(','.join(output))
