n = int(input())

first = second = third = -500

for i in range(n):
    num = int(input())

    if num >= first:
        third = second
        second = first
        first = num
    elif num >= second:
        third = second
        second = num
    elif num >= third:
        third = num

print(f"{first}, {second} and {third}")
