def main():
    # Prompt the user for the target integer
    target = int(input("Enter the integer for the player to guess.\n"))

    # Initialize variables
    guess = None
    attempts = 0

    # Loop until the user guesses correctly
    while guess != target:
        # Prompt the user for a guess
        guess = int(input("Enter your guess.\n"))
        attempts += 1

        # Check if the guess is too high, too low, or correct
        if guess > target:
            print("Too high - try again:")
        elif guess < target:
            print("Too low - try again:")

    # Output the result
    if attempts == 1:
        print("You guessed it in 1 try.")
    else:
        print(f"You guessed it in {attempts} tries.")

# Run the program
if __name__ == "__main__":
    main()
