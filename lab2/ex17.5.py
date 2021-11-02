data = {}
for _ in range(int(input())):
    answer = input()
    data[answer] = data.get(answer)
for _ in range(int(input())):
    a = ''
    ok = False
    for i in input().split('/'):
        if i:
            a = a + '/' + i
        if a in data:
            ok = True
    if ok:
        print('y')
    else:
        print('n')