def sum_digits(num):
    sum = 0
    while (num != 0):
        digit = num % 10
        sum += digit
        num //= 10
    return sum


x = int(input())
y = int(input())
target = int(input())

for i in range(x, y+1):
    if target == sum_digits(i):
        print(i)

############################################
# x = int(input())
# y = int(input())
# target = int(input())
#
# for i in range(x, y+1):
#    temp = str(i)
#
#    if (int(temp[0]) + int(temp[1]) + int(temp[2])) == target:
#        print(i)
