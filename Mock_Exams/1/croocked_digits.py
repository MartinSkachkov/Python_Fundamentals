# def sum_digits(n):
#   return sum(int(digit) for digit in str(n))

def find_sum_digits(number):
    sum_digits = 0

    while number > 0:
        sum_digits += number % 10
        number //= 10

    return sum_digits


n = input()

# determine if the input is int or float
if '.' in n:  # float '-123.4879'
    whole_fraction = n.split('.')  # ['-123', '4879']
    n = whole_fraction[0] + whole_fraction[1]  # '-1234879'
    n = abs(int(n))  # 1234879
else:  # int
    n = abs(int(n))

crooked_digit = find_sum_digits(n)

while crooked_digit > 9:
    crooked_digit = find_sum_digits(crooked_digit)

print(crooked_digit)
