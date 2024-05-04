first_str = input()
second_str = input()

# no need to convert them to lists
first_arr = list(first_str)
second_arr = list(second_str)
flag = False

for i in range(min(len(first_arr), len(second_arr))):
    if first_arr[i] < second_arr[i]:
        print('first')
        flag = True
        break
    elif first_arr[i] > second_arr[i]:
        print('second')
        flag = True
        break

if not flag:
    if len(first_arr) == len(second_arr):
        print('equal')
    elif len(first_arr) < len(second_arr):
        print('first')
    else:
        print('second')

#####################################################

first_str = input()
second_str = input()
flag = False

for i in range(min(len(first_str), len(second_str))):
    if first_str[i] < second_str[i]:
        print('first')
        flag = True
        break
    elif first_str[i] > second_str[i]:
        print('second')
        flag = True
        break

if not flag:
    if len(first_str) == len(second_str):
        print('equal')
    elif len(first_str) < len(second_str):
        print('first')
    else:
        print('second')

#####################################################

word_1 = input()
word_2 = input()

if word_1 < word_2:
    print("first")
elif word_1 > word_2:
    print("second")
elif word_1 == word_2:
    print("equal")
