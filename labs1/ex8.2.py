b = int(input())
a = int(input())
simvol = input()
print(simvol * a)
for i in range(b - 2):
    print(simvol, ' ' * (a - 2), simvol, sep='')
print(simvol * a)