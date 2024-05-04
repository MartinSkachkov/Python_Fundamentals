line = input().split(",")
my_set = []

for el in line:
    # This condition checks whether the current element el is not already in the my_set list.
    if el not in my_set:
        # If el is not in my_set, it means it's a unique element, so it appends el to the my_set list using my_set.append(el).
        my_set.append(el)

print(",".join(my_set))
