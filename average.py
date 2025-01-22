# average.py

def main():
    print("Please enter five numbers.")

    # Initialize a list to store user inputs
    numbers = []

    # Loop to collect five numbers from the user
    for i in range(5):
        number = float(input())  # Convert user input to a float
        numbers.append(number)

    # Calculate the average
    average = sum(numbers) / len(numbers)

    # Print the average
    print("The average of those numbers is:")
    print(average) # No rounding or formatting


if __name__ == "__main__":
    main()
