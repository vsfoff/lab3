q = 0
n = int(input())

while n != 1:
    if n % 2 == 1:
        n -= 1
    elif n % 2 == 0:
        n /= 2
    q += 1
print(int(q))

