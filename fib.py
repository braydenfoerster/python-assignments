def fib(n):
    # Ensure the input is valid
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    # Handle the first two Fibonacci numbers
    if n == 1 or n == 2:
        return 1

    # Initialize variables to store the previous two numbers in the sequence
    prev1, prev2 = 1, 1

    # Use a loop to calculate the Fibonacci number at position n
    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev1, prev2 = prev2, current

    return current

# Example usage
term = fib(17)
print(term)
