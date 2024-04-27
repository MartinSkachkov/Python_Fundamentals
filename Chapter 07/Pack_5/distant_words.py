target = int(input())
n = int(input())

avg_dist = 0
result = []

for i in range(n):
    word = input()

    dist = 0
    for char in word.upper():
        dist += ord(char) - 64

    result.append((word, abs(dist - target)))  # добавяме tuple към list
    avg_dist += abs(dist - target)

for elem in result:
    print(elem[0], elem[1])

print(f'{(avg_dist/n):.2f}')  # деление преди форматиране
