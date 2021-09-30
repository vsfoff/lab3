m = int(input())

n = int(input())

for i in range(1, n + 1):

    for j in range(1, m):
        print(j / i, end=' ')
    print(m / i)
