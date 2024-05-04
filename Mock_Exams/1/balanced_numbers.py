def is_balanced(num):
    return (int(num[0]) + int(num[2]) == int(num[1]))


num = input()
sum_balanced = 0

while is_balanced(num):
    sum_balanced += int(num)
    num = input()

print(sum_balanced)
