longest_name = ''
food = ''

while food != 'END':
    food = input()
    if food != 'END' and len(food) >= len(longest_name):
        longest_name = food

print(longest_name)
