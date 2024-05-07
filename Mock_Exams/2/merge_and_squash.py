n = int(input())
numbers = []

for _ in range(n):
    numbers.append(input())

merged = []
for i in range(n-1):
    merged.append(numbers[i][1] + numbers[i+1][0])

for m in merged:
    print(m, end=' ')
print()

squashed = []
for i in range(n-1):
    first_digit = numbers[i][0]
    last_digit = numbers[i+1][1]
    mid_digit = int(numbers[i][1]) + int(numbers[i+1][0])

    if mid_digit >= 10:
        mid_digit = mid_digit % 10

    squashed.append(first_digit + str(mid_digit) + last_digit)

for s in squashed:
    print(s, end=' ')
print()
