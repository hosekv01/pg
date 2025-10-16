def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)




if __name__ == "__main__":
    print(faktorial(0))
    print(faktorial(1))
    print(faktorial(5))
    print(faktorial(100))