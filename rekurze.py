def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

def faktorial_cyklicky(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print(faktorial(0))
    print(faktorial(1))
    print(faktorial(5))
    print(faktorial(100))

    print(faktorial_cyklicky(0))
    print(faktorial_cyklicky(1))
    print(faktorial_cyklicky(5))
    print(faktorial_cyklicky(100))