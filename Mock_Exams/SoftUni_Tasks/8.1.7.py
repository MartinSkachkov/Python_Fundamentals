sum1 = sum2 = sum3 = 0

n = int(input())

for i in range(n):
    a = int(input())

    if i % 3 == 0:
        sum1 += a
    elif i % 3 == 1:
        sum2 += a
    elif i % 3 == 2:
        sum3 += a

print(f'sum1 = {sum1}')
print(f'sum2 = {sum2}')
print(f'sum3 = {sum3}')