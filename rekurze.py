def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

def faktorial_cyklicky(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print(f"Rekurzivní faktorial 0!: {faktorial(0)}")
    print(f"Rekurzivní faktorial 1!: {faktorial(1)}")
    print(f"Rekurzivní faktorial 5!: {faktorial(5)}")
    print(f"Rekurzivní faktorial 100!: {faktorial(100)}")

    print(f"Iterativní faktorial 0!: {faktorial_cyklicky(0)}")
    print(f"Iterativní faktorial 1!: {faktorial_cyklicky(1)}")
    print(f"Iterativní faktorial 5!: {faktorial_cyklicky(5)}")
    print(f"Iterativní faktorial 100!: {faktorial_cyklicky(100)}")