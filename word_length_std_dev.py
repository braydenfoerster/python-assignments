import math


def word_length_std_dev(text):
    words = text.split()
    n = len(words)

    if n < 2:
        return 0.0  # Standard deviation is undefined for fewer than 2 values

    lengths = [len(word) for word in words]
    mean = sum(lengths) / n
    variance = sum((l - mean) ** 2 for l in lengths) / (n - 1)

    return variance ** 0.5


# Example usage
text = 'There is wisdom in turning as often as possible from the familiar to the unfamiliar it keeps the mind nimble it kills prejudice and it fosters humor'
print(word_length_std_dev(text))