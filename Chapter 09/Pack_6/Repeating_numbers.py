n = int(input())

dp = []

for _ in range(11):
    dp.append(0)

for _ in range(n):
    index = int(input())
    dp[index] += 1

max_rep = 0
number = 0

for i in range(len(dp)):

    if dp[i] == max_rep:
        continue
    elif dp[i] > max_rep:
        max_rep = dp[i]
        number = i

print(number)