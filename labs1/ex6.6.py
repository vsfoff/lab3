n = int(input())
k = 0.0
pi = 3.141592653589793 ** 2
for i in range(1, n + 1):
    k += 1 / (i ** 2)
print(pi / k)
summ = 0
n = int(input())
for i in range(n):
    if i % 2 == 0:
        summ += int(input())
    else:
        summ -= int(input())
print(summ)
