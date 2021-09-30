print("доступные команды: 1. вперед, 2. налево, 3. направо, 4. разворот, 5. стоп")

x = int(input())
y = int(input())
xtec = 0
ytec = 0
count = 0
n = -1
name = input()
while name != "стоп":
    if ytec != y or xtec != x:
        if name == "вперед":
            ytec += int(input())
            if xtec == x and ytec == y:
                n = 1
        elif name == "разворот":
            name = input()
            ytec -= int(input())
            count += 1
            if xtec == x and ytec == y:
                n = 2
        elif name == "налево":
            name = input()
            xtec -= int(input())
            count += 1
            if xtec == x and ytec == y:
                n = 3
        elif name == "направо":
            name = input()
            xtec += int(input())
            count += 1
            if xtec == x and ytec == y:
                n = 4
        count += 1
    name = input()
if n == 1:
    print("север")
elif n == 2:
    print("юг")
elif n == 3:
    print("запад")
else:
    print("восток")
print(count)
