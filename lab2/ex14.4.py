a = list(map(int, input().split()))
xmax = len(a)
ymax = max(a)
print('*'*(xmax + 2))
print('*' + ' '*xmax + '*')
for y in range(1, ymax + 1):
    print(end='*')
    for ak in a:
        if ak >= ymax - y + 1:
            print(end='*')
        else:
            print(end=' ')
    print('*')
