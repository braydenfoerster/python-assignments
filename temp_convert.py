# temp_convert.py

def main():
    print("Please enter a Celsius temperature.")

    # Get the Celsius temperature input from the user
    celsius = float(input())

    # Convert Celsius to Fahrenheit using the formula
    fahrenheit = (9 / 5) * celsius + 32

    # Print the Fahrenheit temperature (up to 7 decimal places)
    print("The equivalent Fahrenheit temperature is:")
    print(fahrenheit)

if __name__ == "__main__":
    main()
