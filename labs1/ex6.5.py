def gcd(a, b):
    while a and b:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


n = int(input())
s_n = 0
s_d = 1
for i in range(n):
    in_n = int(input())
    in_d = int(input())
    s_n = s_n * in_d + in_n * s_d
    s_d *= in_d
g = gcd(s_n, s_d)
print(s_n // g, '/', s_d // g)
