string = {}
for _ in range(int(input())):
    val, key = input().split()
    if key in string:
        string[key].append(val)
    else:
        string[key] = [val]
for _ in range(int(input())):
    key = input()
    if key in string:
        print(*string[key])
    else:
        print('no')