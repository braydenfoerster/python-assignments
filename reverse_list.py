def reverse_list(vals):
    """Takes a list and reverses the order of its elements."""
    left = 0  # Start index
    right = len(vals) - 1  # End index

    while left < right:  # Swap elements until the middle is reached
        vals[left], vals[right] = vals[right], vals[left]
        left += 1
        right -= 1

# Example
vals = [7, -3, 12, 9]
reverse_list(vals)
print(vals)  # This should print [9, 12, -3, 7]
