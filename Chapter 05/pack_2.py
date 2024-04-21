# Guess the Season
month = input()
date = int(input())

if month == "January" or month == "February":
    print("Winter")
elif month == "April" or month == " March":
    print("Spring")
elif month == "July" or month == "August":
    print("Summer")
elif month == "October" or month == "November":
    print("Autumn")
elif month == "March":
    if date < 20:
        print("Winter")
    else:
        print("Spring")
elif month == "June":
    if date < 21:
        print("Spring")
    else:
        print("Summer")
elif month == "September":
    if date < 22:
        print("Summer")
    else:
        print("Autumn")
elif month == "December":
    if date < 21:
        print("Autumn")
    else:
        print("Winter")

# Phone Bill
total_messages = int(input())
total_minutes = int(input())

MONTHLY_BILL = 12
ADD_MIN_COST = 0.1
ADD_MES_COST = 0.06

additional_messages = additional_minutes = 0

if total_messages - 20 > 0:
    additional_messages = total_messages - 20

if total_minutes - 60 > 0:
    additional_minutes = total_minutes - 60

additional_messages_leva = additional_messages * ADD_MES_COST
additional_minutes_leva = additional_minutes * ADD_MIN_COST

print(f"{additional_messages} additional messages for {additional_messages_leva:.2f} levas")
print(f"{additional_minutes} additional minutes for {additional_minutes_leva:.2f} levas")

additional_messages_tax = additional_messages_leva * 0.2
additional_minutes_tax = additional_minutes_leva * 0.2
total_tax = additional_messages_tax + additional_minutes_tax
print(f"{total_tax:.2f} additional taxes")

total_bill = MONTHLY_BILL + total_tax + additional_messages_leva + additional_minutes_leva
print(f"{total_bill:.2f} total bill")
