def erastothenes(n):
    numbers = list(range(2, n + 1))
    primes = []
    while len(numbers) > 0:
        current = numbers[0]
        primes.append(current)
        old_numbers = numbers[1:]
        numbers = []
        for i in old_numbers:
            if i % current != 0:
                numbers.append(i)
    return primes

if __name__ == '__main__':
    print(erastothenes(100))
