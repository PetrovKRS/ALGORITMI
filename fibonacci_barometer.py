def fibonacci_barometer(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_barometer(n - 1) + fibonacci_barometer(n - 2)


if __name__ == '__main__':
    n: int = int(input())
    print(fibonacci_barometer(n + 1))
