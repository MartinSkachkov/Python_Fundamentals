import math

# Print Company Information
name = input()
address = input()
phone_num = input()
fax_num = input()
website = input()
manager_fname = input()
manager_lname = input()
# This line prompts the user to input the first name and last name of the manager separately. It concatenates these two inputs with a space in between to form the full name of the manager, which is stored in the variable manager_name.
# manager_name = input() + ' ' + input()
manager_age = input()
manager_phone_num = input()

print(name)
print("Address:", address)
print("Tel.", phone_num)
print("Fax:", fax_num)
print("Web site:", website)
print(
    f"Manager: {manager_fname} {manager_lname} (age: {manager_age}, tel. {manager_phone_num})"
)

# Circle Perimeter and Area
import math

r = float(input())
area = math.pi * r * r
perimeter = 2 * math.pi * r

print(format(perimeter, ".2f"))
print(format(area, ".2f"))

# This line uses a formatted string to print the value of perimeter with two decimal places using the :.2f format specifier. Similar with area.
# print(f'{perimeter:.2f}')
# print(f'{area:.2f}')

# Converter
mpg = int(input())
KM_PER_MILE = 1.6
LITRES_PER_GALLON = 4.54

km_per_liter = mpg * KM_PER_MILE / LITRES_PER_GALLON
lp100km = 100 // km_per_liter

print(f"{int(lp100km)} litres per 100 km")

# Tips
meal_price = float(input())
tip = 0.1 * meal_price
print(int(meal_price + tip))
