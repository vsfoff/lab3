n = int(input())
s = [[]]
for i in range(n - 1):
    s.append([int(j) for j in input().split()])
station = input().split()
a = int(station[0])
b = int(station[1])
l = s[max(a, b)][min(a, b)]
z = -1
for i in range(n):
    if i != a and i != b:
        if l > s[max(a, i)][min(a, i)] + s[max(i, b)][min(i, b)]:
            l = s[max(i, b)][min(i, b)] + s[max(i, b)][min(i, b)]
            z = i
if z != -1:
    print(z)
else:
    print(a)
