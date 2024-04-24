n = int(input())
sum = 0

for i in range(n):
    num = float(input())
    sum += num

print(f'{(sum/n):.2f}')
