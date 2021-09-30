n = int(input())
count = 0
for i in range(n):
    a = int(input())
    if i == 0:
        print(0)
    if i != 0:
        count += a
        q = count / i
        if a < q:
            print("<")
        else:
            print(">")
