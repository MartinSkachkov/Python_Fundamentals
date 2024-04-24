n = int(input())
sum = 0
min = 10000
max = -10000

for i in range(n):
    num = float(input())
    sum += num

    if num > max:
        max = num

    if num < min:
        min = num

print(f'min={min:.2f}')
print(f'max={max:.2f}')
print(f'sum={sum:.2f}')
print(f'avg={(sum/n):.2f}')
