# The import sys statement in Python is used to import the sys module, which is a built-in module that provides access to various system-specific parameters and functions. In the provided code, the sys module is imported to use the constant sys.maxsize.
import sys

n = int(input())
# It initializes two variables, temp and max_sum, to keep track of the current subarray sum and the maximum subarray sum, respectively. sys.maxsize is used to initialize max_sum with a very small value to ensure any valid input will update it.
temp = 0
max_sum = -sys.maxsize

for i in range(n):
    # Inside the loop, it reads the next element as an integer and stores it in the variable el.
    el = int(input())
    # It updates the current subarray sum (temp) using Kadane's algorithm. This step calculates the maximum sum ending at the current position in the array.
    temp = max(el, el + temp)
    # It updates the maximum subarray sum (max_sum) if the current temp value is greater than the previous max_sum.
    if temp > max_sum:
        max_sum = temp

print(max_sum)
