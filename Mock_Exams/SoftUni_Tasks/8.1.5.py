# април, юни, септември и ноември имат по 30 дни,
# февруари има 28 дни, а останалите имат по 31 дни
days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = int(input())
month = int(input())
leading_zero = False

if month < 10:
    leading_zero = True

days_in_month = days_in_months[month]
after_five_days = day + 5

if after_five_days <= days_in_month:
    if leading_zero:
        print(f'{after_five_days}.0{month}')
    else:
        print(f'{after_five_days}.{month}')
else:
    new_day = after_five_days - days_in_month
    month += 1

    if month == 13:
        month = 1
        leading_zero = True

    if leading_zero:
        print(f'{new_day}.0{month}')
    else:
        print(f'{new_day}.{month}')

