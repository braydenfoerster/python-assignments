def main():
    # Ask the user to enter a positive integer
    number = int(input("Please enter a positive integer: "))

    # Validate that the input is positive
    if number <= 0:
        print("The number must be positive.")
        return

    # Print the factors
    print(f"The factors of {number} are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

# Run the program
if __name__ == "__main__":
    main()
