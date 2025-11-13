import random

x = 1
if x == 1:
    for _ in range(10):  # Loop 10 times
        print(random.randint(1, 100))
else:
    print("x is not 1")