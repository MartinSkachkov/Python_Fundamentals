move_sequnce = input()
x = 0
y = 0

for step in move_sequnce:

    if step == 'L':
        x -= 1
    elif step == 'R':
        x += 1
    elif step == 'U':
        y += 1
    elif step == 'D':
        y -= 1

print(f'({x}, {y})')
