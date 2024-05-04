# It reads a line of integers separated by spaces and stores them in a list called line.
line = [int(el) for el in input().split()]
# It initializes an empty string called output to store the comparison results.
output = ""
# It stores the first element of line in el_0 as a reference for comparison.
el_0 = line[0]
 
# It enters a loop that iterates through the elements in line starting from the second element.
for el in line[1:]:
    # Inside the loop, it compares the current element (el) with the previous element (el_0). If el is greater than el_0, it adds "+" to the output string; otherwise, it adds "-". This builds the output string to represent the sequence of comparisons.
    if el > el_0:
        output += "+"
    else:
        output += "-"
    # It updates the el_0 variable for the next iteration to remember the previous element.
    el_0 = el
 
# After processing all elements in line, it checks if there are consecutive "+" or "--" in the output string. If any are found, it prints "no" because it indicates that the sequence is not strictly increasing. Otherwise, it prints "yes," indicating that the sequence is strictly increasing.
if "--" in output or "++" in output:
    print("no")
else:
    print("yes")