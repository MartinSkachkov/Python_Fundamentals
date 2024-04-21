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
