n = int(input())

DISCOUNT = 0.65
output = []

for i in range(n):
    item_price = float(input())
    item_discount = item_price * DISCOUNT
    new_item_price = item_price - item_discount
    output.append(new_item_price)

for elem in output:
    print(f'{elem:.2f}')
