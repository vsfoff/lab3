string = input()
c = 0
for a in string:
    if a != ' ' and a != '\t':
        c += 1
print(c)