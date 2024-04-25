num = int(input())

# веднъж генериран range-a той не се променя immutable
for i in range(2, (num // 2) + 1):
    if num == 1:  # saves some iterations
        break
    while num % i == 0:
        print(i)
        num //= i
