count = int(input())

for i in range(count):
    inp = input()
    if inp[:4] == '####':
        continue
    if inp[:2] == '%%':
        print(inp[2:])
    else:
        print(inp)


