def count_letters(s):
    # Convert the string to uppercase
    s = s.upper()
    letter_count = {}
    # Loop through every letter in alphabet
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        count = s.count(letter)  # Get the number of times letter appears in s
        if count > 0:  # Only add letters that appear at least once
            letter_count[letter] = count
    return letter_count

# Example usage:
if __name__ == "__main__":
    print(count_letters("AaBb"))  # Output: {'A': 2, 'B': 2}
