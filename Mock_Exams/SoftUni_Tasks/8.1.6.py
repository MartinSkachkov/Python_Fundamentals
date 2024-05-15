num1 = int(input())
num2 = int(input())
num3 = int(input())

POSSIBLE_SUMS = [num1, num2, num3]

if num1+num2 in POSSIBLE_SUMS:
    print(f'{num1} + {num2} = {num1+num2}')
elif num2+num3 in POSSIBLE_SUMS:
    print(f'{num2} + {num3} = {num2+num3}')
elif num1+num3 in POSSIBLE_SUMS:
    print(f'{num3} + {num1} = {num1+num3}')
else:
    print('No')
