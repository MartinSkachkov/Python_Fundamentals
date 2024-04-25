n = int(input())

j = n + 1

for row in range(1, n+1):
    for num in range(row, j):
        print(num, end=' ')
    print()
    j += 1
