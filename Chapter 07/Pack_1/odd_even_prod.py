n = int(input())

# split() без аргументи игнорира много последователни празни места и ги третира като едно
numbers = input().split()  # ['1', '2', '3']

prod_even = 1
prod_odd = 1

for i in range(n):
    if i % 2 == 1:  # i is odd index
        prod_odd *= int(numbers[i])
    else:  # i is even index
        prod_even *= int(numbers[i])

if prod_even == prod_odd:
    print(f'yes {prod_even}')
else:
    print(f'no {prod_even} {prod_odd}')
