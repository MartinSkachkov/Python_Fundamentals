# products in the menu
potato = "01.Potato"
fish = "02.Fish"
apple = "03.Apple"

menu_message = "Menu: Dial only one digit: 1 - Create Order"
print(menu_message)

user_input = int(input())

print(f"Here are our products:\n {potato},\n {fish},\n {apple}")

order_message = "Enter the 2 digit product code to add it to the order"
print(order_message)

template = "Product with code: {} was added to the order"

prod1 = input()
print(template.format(prod1))
prod2 = input()
print(template.format(prod2))
prod3 = input()
print(template.format(prod3))

tanks_message = "Thank you for using our program!"
summary_message = "Summary of your interaction: "
print(tanks_message + "\n" + summary_message)

print(
    f""" Orders: 1 order containing [{prod1},
       {prod2}, {prod3}]"""
)
