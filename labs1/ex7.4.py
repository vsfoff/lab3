tex = input()
k = -1
count = 1
while tex != "СТОП":
    if tex.find("кот") != -1 or tex.find("Кот") != -1 and k == -1:
        k = count
        break
    tex = input()
    count += 1
print(k)
