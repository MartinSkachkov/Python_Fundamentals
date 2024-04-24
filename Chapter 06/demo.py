n = 1
while n <= 10:  # 0 .. 10
    print(n, end=' ')
    n = n + 1
print(n)  # 11
#########################################################
my_seq = range(5)  # def_start = 0; def_step = 1
for n in my_seq:  # n=0; n<5; n++
    print(f'Стойността на n e: {n}')
#########################################################
for i in range(0, 10, 1):  # i=0; i<10; i++
    print(f'Стойността на i e: {i}')
#########################################################
my_name = 'Pesho'
for ch in my_name:  # string iteration
    print(f'{ch} code = {ord(ch)}')
# P code = 80
# e code = 101
# s code = 115
# h code = 104
# o code = 111
#########################################################
for i in range(10):
    if i == 3:
        i += 5
    print(i, end=' ')
print()
# 0 1 2 8 4 5 6 7 8 9

i = 0
while i < 10:
    if i == 3:
        i += 5
    else:
        i += 1
    print(i, end=' ')
#########################################################
for num in range(1, 4):
    for i in range(num):
        print(num, end=' ')
    print()
# 1
# 2 2
# 3 3 3
#########################################################
for i in range(5, 1, 1):  # returns empty sequence (does nothing)
    print(i)
#########################################################
for i in range(30, 20, -2):
    print(i, end=' ')
# 30 28 26 24 22
#########################################################
for i in range(20, 30, -2):  # returns empty sequence (does nothing)
    print(i, end=' ')
#########################################################
for i in range(1, 5, 0):
    print(i, end=' ')
# Output ValueError: range() arg 3 must not be zero
#########################################################
for i in range(-1, -11, -1):
    print(i, end=', ')
# -1, -2, -3, -4, -5, -6, -7, -8, -9, -10
#########################################################
# create list from range()
sample_list = list(range(10, 100, 10))

# iterate and modify list item using range()
# double each list number
# start = 0, stop = list size, step =1
for i in range(0, len(sample_list), 1):
    sample_list[i] = sample_list[i] * 2

#  display updated list
print(sample_list)
# [20, 40, 60, 80, 100, 120, 140, 160, 180]
#########################################################
# If you want to include the end number in the result, i.e.,
# If you want to create an inclusive range, then set the stop = stop+step.
# inclusive range
start = 1
stop = 5
step = 1

# change stop
stop += step

for i in range(start, stop, step):
    print(i, end=' ')
# 1 2 3 4 5
#########################################################
hidden_letter = 'h'

while True:  # endless loop
    your_letter = input()

    if hidden_letter == your_letter:
        print('You guessed correctly!')
        break  # ends the loop
    elif hidden_letter > your_letter:
        print('My letter is larger than your letter!')
    else:
        print('My letter is smaller than your letter!')
#########################################################
