a = []
for i in range(int(input())):
    string = input().split(',')
    a.append(string)
for i in range(int(input())):
    cords = [int(i) for i in input().split(',')]
    d = a[cords[0]]
    word = d[cords[1]]
    print(word)