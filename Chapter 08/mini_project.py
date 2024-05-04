products = ['01.Potato', '02.Fish', '03.Apple', '04.Orange']

print("---Our products list---")
print(products)
print()

orders = []
count_orders = 0
help_requests = []

print('''Please enter a one digit command. Valid commands are: 
"1" for the command create order
"2" for the command list (orders)
"3" for the command request help 
"0" for the command leave or exit the program''')

while True:
    print("----Welcome to main menu----")
    command_code = int(input())

    # Check if the input is an acceptable command code
    if not (command_code in [0, 1, 2, 3]):
        print("Wrong command. Please enter a valid command!")
        continue  # no need to execute below if statements

    if command_code == 1:
        print('Doing create order cmd')
        order_str = ''
        count_orders += 1

        while True:
            print("Enter 2 digit product code or 00 to finish the order")

            two_digit_code = input()
            if two_digit_code == '01':
                print("Adding potato to the order")
                order_str += two_digit_code + ' '
            elif two_digit_code == '02':
                print("Adding fish to the order")
                order_str += two_digit_code + ' '
            elif two_digit_code == '03':
                print("Adding apple to the order")
                order_str += two_digit_code + ' '
            elif two_digit_code == '04':
                print("Adding orange to the order")
                order_str += two_digit_code + ' '
            elif two_digit_code == '00':
                print("The order is finished... Going back to the main menu")
                orders.append(order_str.removesuffix(' '))
                break
            else:
                print("Wrong code")

    elif command_code == 2:
        print("Doing list orders cmd")

        if len(orders) == 0:
            print("You have no orders")
        else:
            print("Here are your orders:")
            for ord_num in range(1, len(orders) + 1):
                print(f'{ord_num} contains: {orders[ord_num-1]}')

    elif command_code == 3:
        print("Doing request help cmd")

        request_ord_num = input()
        if int(request_ord_num) in range(1, count_orders + 1):
            print(f"""the order ({request_ord_num}) you want help with contains: {orders[int(request_ord_num)-1]}
                Continue(c) or Discard(d)""")

            while True:
                choice = input()
                if choice == 'c':
                    help_requests.append(int(request_ord_num))
                    print(f"Current status of help requests: {help_requests}")
                    break
                elif choice == 'd':
                    break
                else:
                    print("Wrong input. Enter (c) or (d)")
                    continue
        else:
            print("The entered number is not a valid order number! Returning back to main menu.")
    elif command_code == 0:
        print("Thank you for using our program!\nSummary of your interaction:")

        print("----Your orders----")
        cnt = 1
        for order in orders:
            print(f'{cnt}: {order}')
            cnt += 1

        print("----Help requests----")
        for h_r in help_requests:
            print(f'You need help with order {h_r}')

        break
