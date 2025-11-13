def fibonacci(maximum):
    result = []
    a, b = 1, 1
    while a <= maximum:
        result.append(a)
        a, b = b, a + b
    return result


if __name__ == "__main__":
    import sys
    maximum = int(sys.argv[1])
    print(fibonacci(maximum))