num = int(input())
r, rr, dd = 1, [], []

while r not in rr:
    rr.append(r)
    dd.append(10 * r // num)
    r = 10 * r % num
print(*dd[rr.index(r):])
