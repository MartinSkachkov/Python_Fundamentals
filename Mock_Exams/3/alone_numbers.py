def alone_numbers(arr, target):
    # Copy the array
    new_arr = arr.copy()
    
    # Iterate over the array
    for i in range(1, len(arr) - 1):
        # Check if the current element is the target and is alone
        if arr[i] == target and arr[i-1] != target and arr[i+1] != target:
            # Replace the element with the larger of its neighbors
            new_arr[i] = max(arr[i-1], arr[i+1])
            
    return new_arr

arr = [int(num) for num in input().split(',')]
target = int(input())

print(alone_numbers(arr,target))