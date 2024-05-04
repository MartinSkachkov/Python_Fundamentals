n = int(input())

letters = []

for i in range(n):
    user_input = input()
    letters.append(user_input)

ascii = []

for letter in letters:
    ascii.append(ord(letter))

letters.clear()
ascii.sort()

for sym in ascii:
    letters.append(chr(sym))

print(letters)
