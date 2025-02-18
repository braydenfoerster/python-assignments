def list_of_primes_up_to(limit=100):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    num = 2
    while num * num <= limit:
        if primes[num]:
            for multiple in range(num * num, limit + 1, num):
                primes[multiple] = False
        num += 1

    return [i for i in range(limit + 1) if primes[i]]


# Example usage
print(list_of_primes_up_to(1000))