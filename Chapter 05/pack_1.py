# Exchange if Greater
a = input()
b = input()

a = int(a) if a.isdigit() else float(a)
b = int(b) if b.isdigit() else float(b)

if a > b:
    temp = a
    a = b
    b = temp

print(a, b)


# Bonus Score
score = int(input())

if 1 <= score <= 3:
    score = score * 10
elif 4 <= score <= 6:
    score = score * 100
elif 7 <= score <= 9:
    score = score * 1000
else:
    score = "invalid score"
print(score)

# Check for Play Card
card = input()

if card.isdigit() and 2 <= int(card) <= 10:
    print("yes")
elif card == "Q" or card == "J" or card == "K" or card == "A":
    print("yes")
else:
    print("no")
