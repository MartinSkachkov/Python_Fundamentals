line = input().split(",")
 
negatives = []
zeros = []
positives = []
 
for el in line:
    if int(el) < 0:
        negatives.append(el)
    elif int(el) == 0:
        zeros.append(el)
    else:
        positives.append(el)
 
print(",".join(negatives + zeros + positives))