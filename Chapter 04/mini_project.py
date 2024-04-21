user_input = input("Please enter a 3 digit code. All characters must be digits\n")

if len(user_input) != 3:
    print("Invalid number of characters in the input: must be 3")
elif user_input.isdigit():
    print("Input accepted")
else:
    print("Input must contain digits only!")
