def multiply(a, b=1):
    """Recursively multiplies two positive integers using addition."""
    if b == 0:
        return 0  # Base case: anything times 0 is 0
    if b == 1:
        return a  # Base case: anything times 1 is itself

    return a + multiply(a, b - 1)


# Example usage
if __name__ == "__main__":
    result = multiply(a=7, b=4)  # Using keyword arguments
    print(result)
