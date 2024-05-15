bricks = int(input())
workers = int(input())
capacity = int(input())

one_course_work = workers * capacity

if bricks % one_course_work > 0:
    result = bricks // one_course_work + 1
else:
    result = bricks // one_course_work

print(result)