def main():
    # Ask the user for the number of integers they would like to enter
    num_integers = int(input("How many integers would you like to enter?\n"))

    # Prompt the user to enter the integers
    print(f"Please enter {num_integers} integers.")

    # Read the first integer and initialize min and max with it
    first_num = int(input())
    min_num = first_num
    max_num = first_num

    # Loop through the rest of the integers, updating min and max as needed
    for _ in range(num_integers - 1):
        current_num = int(input())
        if current_num < min_num:
            min_num = current_num
        if current_num > max_num:
            max_num = current_num

    # Print the results
    print(f"min: {min_num}")
    print(f"max: {max_num}")

# Run the program
if __name__ == "__main__":
    main()
