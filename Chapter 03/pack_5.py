# Seconds
days = int(input())
hours = int(input())
minutes = int(input())
seconds = int(input())

total_seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds
print(total_seconds)

# Interest
deposited_sum = int(input())

first_year_income = deposited_sum * 0.05
first_year_deposit = deposited_sum + first_year_income
print(format(round(first_year_deposit, 2), ".2f"))

second_year_income = first_year_deposit * 0.05
second_year_deposit = first_year_deposit + second_year_income
print(format(round(second_year_deposit, 2), ".2f"))

thrid_year_income = second_year_deposit * 0.05
third_year_deposit = second_year_deposit + thrid_year_income
print(format(round(third_year_deposit, 2), ".2f"))

# Quadratic Equation
# Imports the math module to access mathematical functions, particularly the sqrt() function for square root calculation
import math

a = float(input())
b = float(input())
c = float(input())

discriminant = (b * b) - (4 * a * c)

root1 = (-b - math.sqrt(discriminant)) / (2 * a)
root2 = (-b + math.sqrt(discriminant)) / (2 * a)

# Print the (root1 + 0) and (root2 + 0) with one decimal place using an f-string
# The +0 is added to fix an issue where negative zero is printed with its minus sign.
print(f"x1={root1 + 0:.1f}")
print(f"x2={root2 + 0:.1f}")

# Sum Digits
n = int(input())
fourth_digit = n % 10
n //= 10
third_digit = n % 10
n //= 10
second_digit = n % 10
n //= 10

print(n + second_digit + third_digit + fourth_digit)
