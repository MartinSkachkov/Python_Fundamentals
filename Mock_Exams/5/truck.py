small_bottles = int(input())
big_bottles = int(input())
truck_capacity = int(input())

while truck_capacity > 0 and big_bottles != 0:
    truck_capacity -= 5
    big_bottles -= 1

if truck_capacity < 0:
    # remove a big bottle for smaller ones
    truck_capacity += 5
    big_bottles += 1

if truck_capacity > small_bottles:
    print(-1)
else:
    print(truck_capacity)