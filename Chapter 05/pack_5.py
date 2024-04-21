# Calculate Change
item_price = float(input())
paid_amount = float(input())

change = paid_amount * 100 - item_price * 100

if change // 100:
    n = change // 100
    print(f"{n:.0f} x 1 lev")
    change -= n * 100

if change // 50:
    n = change // 50
    print(f"{n:.0f} x 50 stotinki")
    change -= n * 50

if change // 20:
    n = change // 20
    print(f"{n:.0f} x 20 stotinki")
    change -= n * 20

if change // 10:
    n = change // 10
    print(f"{n:.0f} x 10 stotinki")
    change -= n * 10

if change // 5:
    n = change // 5
    print(f"{n:.0f} x 5 stotinki")
    change -= n * 5

if change // 2:
    n = change // 2
    print(f"{n:.0f} x 2 stotinki")
    change -= n * 2

if change // 1:
    n = change // 1
    print(f"{n:.0f} x 1 stotinka")
    change -= n * 1

# Chinese Zodiac
year = int(input())

if year % 12 == 8:
    print("Dragon")
elif year % 12 == 9:
    print("Snake")
elif year % 12 == 10:
    print("Horse")
elif year % 12 == 11:
    print("Sheep")
elif year % 12 == 0:
    print("Monkey")
elif year % 12 == 1:
    print("Rooster")
elif year % 12 == 2:
    print("Dog")
elif year % 12 == 3:
    print("Pig")
elif year % 12 == 4:
    print("Rat")
elif year % 12 == 5:
    print("Ox")
elif year % 12 == 6:
    print("Tiger")
elif year % 12 == 7:
    print("Hare")
