def square_list(nums):
    """Takes a list of numbers and replaces each value with its square."""
    for i in range(len(nums)):  # Loop through each index in the list
        nums[i] = nums[i] * nums[i]  # Square the value at that index

# Example
nums = [7, -3, 12, 9]
square_list(nums)
print(nums)  # This should print [49, 9, 144, 81]
