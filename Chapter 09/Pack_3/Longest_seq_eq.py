n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))

dp = []
for _ in range(n):
    dp.append(0)
dp[0] = 1

most_repeated = 1
max_val = 0
for i in range(1, len(lst)):
    if lst[i-1] == lst[i]:
        dp[i] = dp[i-1] + 1

        # find the most repeated consecutive elem and which one it is
        if dp[i] > most_repeated:
            most_repeated = dp[i]
            max_val = lst[i]
    else:
        dp[i] = 1

print(most_repeated)
# print(max_elem, max_val)
