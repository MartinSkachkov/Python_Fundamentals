lst = input().split(',')

sum = 0
for elem in lst:
    sum += int(elem)

avg = sum / len(lst)

below = []
above = []
for elem in lst:
    if int(elem) < avg:
        below.append(elem)
    elif int(elem) > avg:
        above.append(elem)

print(f"avg: {avg:.2f}\nbelow: {','.join(below)}\nabove: {','.join(above)}")
