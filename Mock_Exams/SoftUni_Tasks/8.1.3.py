def calc(first, second, point):
    dist1 = abs(point - first)
    dist2 = abs(second - point)

    if dist1 > dist2:
        print(dist2)
    else:
        print(dist1)


end1 = int(input())
end2 = int(input())
point = int(input())

first = min(end1, end2)
second = max(end1, end2)

if point >= first and point <= second:
    print('in')
    calc(first, second, point)
else:
    print('out')
    calc(first, second, point)
