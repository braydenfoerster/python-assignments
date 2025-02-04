def find_median(numbers):
    numbers.sort()
    n = len(numbers)

    if n % 2 == 1:
        return numbers[n // 2]
    else:
        middle1 = numbers[n // 2 - 1]
        middle2 = numbers[n // 2]
        return (middle1 + middle2) / 2


some_nums = [13, 7, -3, 82, 4]
result = find_median(some_nums)
print(result)
