# Biggest of Five
# var. 1
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

if n1 >= n2 and n1 >= n3 and n1 >= n4 and n1 >= n5:
    print(n1)
elif n2 >= n1 and n2 >= n3 and n2 >= n4 and n2 >= n5:
    print(n2)
elif n3 >= n1 and n3 >= n2 and n3 >= n4 and n3 >= n5:
    print(n3)
elif n4 >= n1 and n4 >= n2 and n4 >= n3 and n4 >= n5:
    print(n4)
else:
    print(n5)

# var. 2
max_num = -200  # given by the constraints

y1 = int(input())
if y1 >= max_num:
    max_num = y1

y2 = int(input())
if y2 >= max_num:
    max_num = y2

y3 = int(input())
if y3 >= max_num:
    max_num = y3

y4 = int(input())
if y4 >= max_num:
    max_num = y4

y5 = int(input())
if y5 >= max_num:
    max_num = y5

print(max_num)

# Sort Three Numbers
x1 = int(input())
x2 = int(input())
x3 = int(input())

first = second = third = None

if x1 >= x2 and x1 >= x3:
    first = x1
    if x2 >= x3:
        second = x2
        third = x3
    else:
        second = x3
        third = x2
elif x2 >= x1 and x2 >= x3:
    first = x2
    if x1 >= x3:
        second = x1
        third = x3
    else:
        second = x3
        third = x1
else:
    # x3 is max
    first = x3
    if x2 >= x1:
        second = x2
        third = x1
    else:
        second = x1
        third = x2

print(first, second, third)

# Digit as Word
digit = int(input())

match int(digit):
    case 0:
        print('zero')
    case 1:
        print('one')
    case 2:
        print('two')
    case 3:
        print('three')
    case 4:
        print('four')
    case 5:
        print('five')
    case 6:
        print('six')
    case 7:
        print('seven')
    case 8:
        print('eight')
    case 9:
        print('nine')
    case _:
        print('not a digit')
