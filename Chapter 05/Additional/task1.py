# Given a variable a (containing any value), re-assign the value "N/A" if a is None,
# and leave a unchanged otherwise. Use an if...else... statement.
a = 5

if a == None:
    a = 'N/A'

print(a)

# Do the same thing as Question 1, but this time use a ternary operator.
a = 'N/A' if a == None else a
print(a)

# Given an credit score score, assign a string value to another variable rating based on the following scale:
# [0, 580) --> Poor
# [580, 670) --> Fair
# [670, 740) --> Good
# [740, 800) --> Very Good
# [800, 850] --> Excellent
score = int(input())
rating = None

if 0 <= score < 580:
    rating = 'Poor'
elif 580 <= score < 670:
    rating = 'Fair'
elif 670 <= score < 740:
    rating = 'Good'
elif 740 <= score < 800:
    rating = 'Very Good'
elif 800 <= score <= 850:
    rating = 'Excellent'
else:
    rating = 'invalid rating'

print(rating)

# Given an elapsed time (in seconds), write code to set a variable magnitude based on the following conditions:
#
# if elapsed time is less than 1 minute, magnitude --> 'seconds'
# if elapsed time is more than 1 minute, but less than 1 hour, magnitude --> 'minutes'
# if elapsed time is more than 1 hour, but less than 1 day, magnitude --> 'hours'
# if elapsed time is more than 1 day, but less than 1 week: magnitude --> 'days'
# if elapsed time is more than 1 week, magnitude --> 'weeks'
elapsed_time = int(input())
magnitude = None

MINUTE_SEC = 60
HOUR_SEC = 60 * MINUTE_SEC
DAY_SEC = 24 * HOUR_SEC
WEEK_SEC = 7 * DAY_SEC

if elapsed_time < MINUTE_SEC:
    magnitude = 'seconds'
elif elapsed_time < HOUR_SEC:
    magnitude = 'minutes'
elif elapsed_time < DAY_SEC:
    magnitude = 'hours'
elif elapsed_time < WEEK_SEC:
    magnitude = 'days'
else:
    magnitude = 'weeks'

print(magnitude)
