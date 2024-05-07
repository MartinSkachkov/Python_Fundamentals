digits = [int(digit) for digit in input()]

res1 = digits[0] * digits[1] * digits[2]
res2 = digits[0] * digits[1] + digits[2]
res3 = digits[0] + digits[1] * digits[2]
res4 = digits[0] + digits[1] + digits[2]

print(max(res1, res2, res3, res4))
