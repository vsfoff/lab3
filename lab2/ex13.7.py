n = int(input())
list = []
for i in range(n):
    list.append(input())
k = int(input())
a = 0
print(list[0])
del list[0]
for i in range(n):
    if len(list) > a + k - 1:
        a += k - 1
        print(list[a])
        del list[a]
    else:
        a = 0
        if len(list) > a:
            print(list[a])
            del list[a]