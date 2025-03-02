def count_letters(s):
    letter_count = {}

    for char in s:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):  # Check if it's a letter
            char = char.upper()  # Convert to uppercase
            if char in letter_count:
                letter_count[char] += 1  # count if the letter already exists
            else:
                letter_count[char] = 1  # Add letter to dictionary

    return letter_count


# Example usage
if __name__ == "__main__":
    print(count_letters("AaBb"))  # Output: {'A': 2, 'B': 2}