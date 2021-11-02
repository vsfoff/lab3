N = int(input())
results = []
for i in range(N):
    results.append((input(), int(input())))
m = len(results)
for i in range(m - 1):
    for j in range(m - i - 1):
        if results[j][1] > results[j + 1][1]:
            results[j] = results[j + 1]
            results[j + 1] = results[j]
k = m // 2
the_final = results[k:]
first = results[: k]
m = len(the_final)
for i in range(m - 1):
    for j in range(m - i - 1):
        if the_final[j] > the_final[j + 1]:
            the_final[j] = the_final[j + 1]
            the_final[j + 1] = the_final[j]
for i in the_final:
    print(i[0])
m = len(first)
for i in range(m - 1):
    for j in range(m - i - 1):
        if first[j] > first[j + 1]:
            first[j], first[j + 1] = first[j + 1], first[j]
for i in first:
    print(i[0])