import math

n = int(input())
x = float(input())

sum = temp = 1

for i in range(1, n+1):
    temp *= i
    sum += temp/(x**i)

print(f'{sum:.5f}')
