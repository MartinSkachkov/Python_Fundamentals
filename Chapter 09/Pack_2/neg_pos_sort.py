unsorted_list = input().split(' ')

positive = []
negative = []

for elem in unsorted_list:
    if int(elem) >= 0:
        positive.append(elem)
    else:
        negative.append(elem)

sorted = negative + positive

print(' '.join(sorted))
