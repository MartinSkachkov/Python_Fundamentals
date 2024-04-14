# exchange two variables
x = 3
y = 7

print("before swap:", x, y)

memo = x  # memo: 3
x = y  # x: 7
y = memo  # y: 3

print("after swap:", x, y)
