n = [int(digit) for digit in input()]

odd_sum = 0
even_sum = 0

for digit in n:
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit

if even_sum > odd_sum:
    print(f'{even_sum} energy drinks')
elif odd_sum > even_sum:
    print(f'{odd_sum} cups of coffee')
else:
    print(f'{even_sum} of both')
