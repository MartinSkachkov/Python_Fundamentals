# Beer time
input = input()

if " " in input and ":" in input and len(input.split(' ')) != 2:
    print('invalid time')

# input = '2:59 AM' -> ['2:59', 'AM']
time = input.split(' ')[0]  # '2:59'
designator = input.split(' ')[1]  # 'AM'

# time = '2:59' -> ['2', '59']
hours = int(time.split(':')[0])  # '2'
minutes = int(time.split(':')[1])  # '59'

# check for valid time format
if not (1 <= hours <= 12 and 0 <= minutes <= 59 and (designator == 'AM' or designator == 'PM')):
    print('invalid time')

if ((designator == 'PM' and 1 <= hours <= 11 and 0 <= minutes <= 59) or
        (designator == 'AM' and (hours == 1 or hours == 2 or hours == 12) and 0 <= minutes <= 59)):
    print('beer time')
else:
    print('non-beer time')

# Numbers as Words
num = int(input())

if num == 0:
    print('zero')

# броят на стотиците, десетиците, единиците
hundreds = num // 100
tens = (num - (hundreds * 100)) // 10
ones = (num - (hundreds * 100) - (tens*10)) // 1

output_for_hundreds = ''
output_for_tens = ''
output_for_ones = ''

if ones > 0 and tens != 1:
    if ones == 1:
        output_for_ones = 'one'
    if ones == 2:
        output_for_ones = 'two'
    if ones == 3:
        output_for_ones = 'three'
    if ones == 4:
        output_for_ones = 'four'
    if ones == 5:
        output_for_ones = 'five'
    if ones == 6:
        output_for_ones = 'six'
    if ones == 7:
        output_for_ones = 'seven'
    if ones == 8:
        output_for_ones = 'eight'
    if ones == 9:
        output_for_ones = 'nine'

if tens == 1:
    output_for_ones = ''

    if ones == 1:
        output_for_ones = 'eleven'
    if ones == 2:
        output_for_ones = 'twelve'
    if ones == 3:
        output_for_ones = 'thirteen'
    if ones == 4:
        output_for_ones = 'fourteen'
    if ones == 5:
        output_for_ones = 'fifteen'
    if ones == 6:
        output_for_ones = 'sixteen'
    if ones == 7:
        output_for_ones = 'seventeen'
    if ones == 8:
        output_for_ones = 'eighteen'
    if ones == 9:
        output_for_ones = 'nineteen'

if tens >= 2:
    if tens == 2:
        output_for_tens = 'twenty'
    if tens == 3:
        output_for_tens = 'thirty'
    if tens == 4:
        output_for_tens = 'fourty'
    if tens == 5:
        output_for_tens = 'fifty'
    if tens == 6:
        output_for_tens = 'sixty'
    if tens == 7:
        output_for_tens = 'seventy'
    if tens == 8:
        output_for_tens = 'eighty'
    if tens == 9:
        output_for_tens = 'ninety'

    if output_for_ones:
        output_for_tens += ' '

if hundreds > 0:
    if hundreds == 1:
        output_for_hundreds = 'one'
    if hundreds == 2:
        output_for_hundreds = 'two'
    if hundreds == 3:
        output_for_hundreds = 'three'
    if hundreds == 4:
        output_for_hundreds = 'four'
    if hundreds == 5:
        output_for_hundreds = 'five'
    if hundreds == 6:
        output_for_hundreds = 'six'
    if hundreds == 7:
        output_for_hundreds = 'seven'
    if hundreds == 8:
        output_for_hundreds = 'eight'
    if hundreds == 9:
        output_for_hundreds = 'nine'

    output_for_hundreds += ' hundred'
    if output_for_tens or output_for_ones:
        output_for_hundreds += ' and '

print(f'{output_for_hundreds}{output_for_tens}{output_for_ones}')
