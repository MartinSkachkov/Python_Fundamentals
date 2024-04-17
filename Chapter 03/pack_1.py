# Hello, Telerik Academy
# We use the function print() to print the information.
print("Hello, Telerik Academy!")

# Hello you
# The input() function is used to gather user input from the console. Whatever the user types is stored as a string in the name variable.
name = input()
# This line uses the print() function to display a message containing the user's input. The f before the string indicates that it's an f-string, which allows you to embed expressions within curly braces {} directly in the string.
print(f"Hello, {name}!")

# Sum of Three Number
# This line prompts the user to input a value, which is expected to be an integer. The input() function reads the user's input as a string, and the int() function is used to convert that string into an integer. The resulting integer value is stored in the variable n1.
n1 = int(input())
n2 = int(input())
n3 = int(input())
# This line calculates the sum of the three integer values stored in n1, n2, and n3, and then uses the print() function to display the result in the console.
print(n1 + n2 + n3)
