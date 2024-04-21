# Int, Double, String
variable_type = input()

if variable_type == 'integer':
    int_input = int(input())
    print(f'{int_input + 1}')
elif variable_type == 'real':
    float_input = float(input())
    print(f'{float_input + 1:.2f}')
elif variable_type == 'text':
    text = input()
    print(text + '*')

# Biggest of Three
a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

# Multiplication Sign
a = float(input())
b = float(input())
c = float(input())

product = a*b*c

if product > 0:
    print('+')
elif product == 0:
    print(0)
else:
    print('-')
