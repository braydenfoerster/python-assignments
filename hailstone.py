def hailstone(n):
    # Ensure the input is valid
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    steps = 0

    # Continue until the sequence reaches 1
    while n != 1:
        if n % 2 == 0:  # If n is even
            n //= 2
        else:           # If n is odd
            n = 3 * n + 1
        steps += 1

    return steps

# Example usage
answer = hailstone(1000)
print(answer)
