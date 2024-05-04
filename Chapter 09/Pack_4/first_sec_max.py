lst = input().split(' ')

first_max = -100
second_max = -100

for elem in lst:
    if int(elem) > second_max:
        second_max = int(elem)

    if int(elem) >= first_max:
        second_max = first_max  # ignoring the first elem
        first_max = int(elem)

print(f'{first_max} {second_max}')
