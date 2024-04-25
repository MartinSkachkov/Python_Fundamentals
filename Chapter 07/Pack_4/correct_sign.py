n = int(input())
num = int(input())
output = str(num)


for i in range(n-1):
    prev = num
    num = int(input())
    if prev > num:
        output += f'>{num}'
    elif prev < num:
        output += f'<{num}'
    else:
        output += f'={num}'

print(output)
