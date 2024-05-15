title = input()
n = int(input())

for _ in range(n):
    sub = input()
    rest = ''
    has_sub = False
    i = 0

    for letter in title:
        if i < len(sub) and letter == sub[i]:
            i += 1
            has_sub = True
        else:
            rest += letter

    if has_sub and i == len(sub):
        title = rest
        print(rest)
    else:
        print('No such title found!')
