import math  # We’re not actually using this, but it’s good to have for math-related functions


def word_length_std_dev(text):
    """
    Calculates the standard deviation of word lengths in a given text.

    Standard deviation basically tells us how much the word lengths in the text vary
    from the average word length.

    :param text: A string containing words
    :return: Standard deviation of word lengths as a float
    """

    # Split the text into words (splitting by spaces)
    words = text.split()

    # Get the number of words in the text
    n = len(words)

    # If there are fewer than 2 words, we can’t calculate a meaningful standard deviation
    if n < 2:
        print("Not enough words to calculate the standard deviation. Try adding more words!")
        return 0.0

        # Get the length of each word and store it in a list
    lengths = [len(word) for word in words]

    # Calculate the average (mean) word length
    mean = sum(lengths) / n

    # Calculate variance (which tells us how spread out the word lengths are)
    # We square the differences from the mean, sum them up, and divide by (n - 1) (to correct for small sample sizes)
    variance = sum((l - mean) ** 2 for l in lengths) / (n - 1)

    # Standard deviation is just the square root of the variance
    return variance ** 0.5


# Example usage
text = "There is wisdom in turning as often as possible from the familiar to the unfamiliar it keeps the mind nimble it kills prejudice and it fosters humor"

# Run the function and print the result
print(word_length_std_dev(text))