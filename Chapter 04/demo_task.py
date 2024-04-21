# Dog years

hy = int(input())
dy = None

if hy <= 2:
    dy = hy * 10
else:
    hy -= 2
    dy = 20 + (4 * hy)

print(dy)

# chess board
label = input()
rank = int(input())

rank_parity = "even" if rank % 2 == 0 else "odd"

if rank_parity == "odd":
    if label in ["a", "c", "e", "g"]:
        print("dark")
    else:
        print("light")
else:
    if label in ["b", "d", "f", "h"]:
        print("dark")
    else:
        print("light")

# Read the input for the rank and convert it to a numerical value (1 to 26) using ASCII value manipulation and the ord() function.
rank = ord(input()) - 96

# Read the input for the label.
label = int(input())

# Check if both the label and rank have the same odd/even parity.
if (label % 2 == 1 and rank % 2 == 1) or (label % 2 == 0 and rank % 2 == 0):
    print(
        "dark"
    )  # Print "dark" if both label and rank have the same parity (odd or even).
else:
    print(
        "light"
    )  # Print "light" if label and rank have different parities (odd and even).
