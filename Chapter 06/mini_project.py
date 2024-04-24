print('''Please enter a one digit command. Valid commands are: 
"1" for the command create order
"2" for the command list (orders)
"3" for the command request help 
"0" for the command leave or exit the program''')

while True:
    command_code = int(input())

    # Check if the input is an acceptable command code
    if not (command_code in [0, 1, 2, 3]):
        print("Wrong command. Please enter a valid command!")
        continue  # no need to execute below if statements

    if command_code == 1:
        print('Doing create cmd')

        while True:
            print("Enter 2 digit product code or 00 to finish the order")

            two_digit_code = input()
            if two_digit_code == '01':
                print("Adding potato to the order")
            elif two_digit_code == '02':
                print("Adding fish to the order")
            elif two_digit_code == '00':
                print("The order is finished... Going back to the main menu")
                break
            else:
                print("Wrong code")

    elif command_code == 2:
        print("Doing list cmd")
    elif command_code == 3:
        print("Doing request cmd")
    elif command_code == 0:
        print("Thank you")
        break
