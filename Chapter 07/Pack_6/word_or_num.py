n = int(input())
num = 0
words = ''

for i in range(n):
    user_input = input()

    if user_input.isdigit():
        num += int(user_input)
    else:
        if words == '':
            words += user_input
        else:
            words += '-' + user_input

if len(words) == 0:
    print('no words')
else:
    print(words)

print(num)

#########################################
n = int(input())
num = 0
words = []

for i in range(n):
    user_input = input()

    if user_input.isdigit():
        num += int(user_input)
    else:
        words.append(user_input)

if not words:
    print('no words')
else:
    print('-'.join(words))

print(num)
