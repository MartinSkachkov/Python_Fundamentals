def is_wave1(lst):

    if len(lst) == 1:
        return 'yes'

    # we have at least 2 numbers
    i = 1
    while i < len(lst):

        if i % 2 == 1:
            if int(lst[i-1]) > int(lst[i]):
                i += 1
            else:
                return 'no'
        else:
            if int(lst[i-1]) < int(lst[i]):
                i += 1
            else:
                return 'no'

    return 'yes'


def is_wave2(lst):

    if len(lst) == 1:
        return 'yes'

    # we have at least 2 numbers
    i = 1
    while i < len(lst):

        if i % 2 == 1:
            if int(lst[i-1]) < int(lst[i]):
                i += 1
            else:
                return 'no'
        else:
            if int(lst[i-1]) > int(lst[i]):
                i += 1
            else:
                return 'no'

    return 'yes'


lst = input().split(' ')
res = ((True if is_wave1(lst) == 'yes' else False) or (True if is_wave2(lst) == 'yes' else False))

if res:
    print('yes')
else:
    print('no')
