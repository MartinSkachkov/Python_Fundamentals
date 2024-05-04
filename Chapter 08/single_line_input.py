letters = input().split(',')
seen = []

for letter in letters:
    if letter in seen:
        print(f'{letter} is duplicate!')
    else:
        seen.append(letter)

print(seen)