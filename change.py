# change.py

def main():
    print("Please enter an amount in cents less than a dollar.")

    # Get the amount in cents from the user
    cents = int(input())

    # Calculate the number of quarters
    quarters = cents // 25
    cents %= 25

    # Calculate the number of dimes
    dimes = cents // 10
    cents %= 10

    # Calculate the number of nickels
    nickels = cents // 5
    cents %= 5

    # The remaining cents are pennies
    pennies = cents

    # Print the results
    print("Your change will be:")
    print(f"Q: {quarters}")
    print(f"D: {dimes}")
    print(f"N: {nickels}")
    print(f"P: {pennies}")


if __name__ == "__main__":
    main()
