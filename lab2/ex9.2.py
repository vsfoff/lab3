from collections import Counter  # подсчет количества

m = int(input())
familii = []
for i in range(m):
    for j in range(int(input())):
        q = input()
        familii.append(q)  # добавление аргумента в конец списка
list1 = dict(Counter(familii))  # словарь
for who in list1:
    if list1.get(who) == m:
        print(who)
