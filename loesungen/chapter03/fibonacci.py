def fibonacci(n):
    result = []
    for i in range(0, n):
        if len(result) < 2:
            result.append(1)
        else:
            result.append(result[i - 2] + result[i - 1])
    return result

if __name__ == '__main__':
    n = input("Wie viele Elemente der Fibonacci-Folge? ")
    print(fibonacci(int(n)))

