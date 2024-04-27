n = int(input())

num = 0
words = ''
user_input = None
output = []

for i in range(n):
    if i == 0:
        user_input = input()

        if user_input.isdigit() or user_input[1:].isdigit():
            num += int(user_input)
        else:
            words += user_input
    else:
        prev = user_input
        user_input = input()

        if user_input.isdigit() or user_input[1:].isdigit():
            num += int(user_input)
        else:
            if words == '':
                words += user_input
            else:
                words += '-' + user_input

        if (prev.isdigit() or prev[1:].isdigit()) and not (user_input.isdigit() or user_input[1:].isdigit()):
            output.append(num)  # print(num)
            num = 0
        elif not (prev.isdigit() or prev[1:].isdigit()) and (user_input.isdigit() or user_input[1:].isdigit()):
            output.append(words)  # print(words)
            words = ''

if num != 0:
    output.append(num)  # print(num)
else:
    output.append(words)  # print(words)

for elem in output:
    print(elem)
