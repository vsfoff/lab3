kolvo = int(input("kol-vo:"))
list1 = set()
list2 = set()

for i in range(kolvo):
    famil = str(input())
    if famil in list1:
        list2.add(famil)
    else:
        list1.add(famil)
rez = list1 - list2
itog = kolvo - len(rez)
print(itog)