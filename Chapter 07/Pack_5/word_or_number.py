input = input()
reversed_str = ''
input_len = len(input)

# Check if the last character in input is digit
if input[-1].isdigit():
    temp = float(input) // 1  # 3.14 -> 3 & 3.00 -> 3

    # Check if the number is int
    if float(input) - temp == 0:
        print(int(input)+1)
    else:  # It's a float
        print(float(input)+1)
else:
    for i in range(input_len - 1, -1, -1):
        reversed_str += input[i]
    print(reversed_str)
