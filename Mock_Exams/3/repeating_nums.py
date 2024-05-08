# ver 1
n = int(input())

numbers = []

for _ in range(n):
    numbers.append(int(input()))

dp = [0 for _ in range(11)]

for elem in numbers:
    dp[elem] += 1

most_repeating_count = 0
most_repeating_number = 0

for i in range(11):
    if dp[i] > most_repeating_count:
        most_repeating_count = dp[i]
        most_repeating_number = i

print(most_repeating_number)

##################################################
# ver 2
n = int(input())

numbers = []

for _ in range(n):
    numbers.append(int(input()))

most_repeating_count = 0
most_repeating_number = 0

for i in range(1, 11):
    if numbers.count(i) > most_repeating_count:
        most_repeating_count = numbers.count(i)
        most_repeating_number = i

print(most_repeating_number)
