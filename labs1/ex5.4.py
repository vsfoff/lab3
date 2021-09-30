import random

n = int(input())

while n > 0:
    n1 = n % 4
    if n1 == 0:
        n1 = random.randint(1, 3)
    n -= n1
    print("vyv1: ", n1, n)

    if n == 0:
        print("ii vin")
    else:
        n1 = int(input())
        n -= n1
        print("vyv2: ", n1, n)
        if n == 0:
            print("u win")
