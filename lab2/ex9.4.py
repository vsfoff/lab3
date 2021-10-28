kolvo_holod = int(input())
holodilnik = set()
prod = set()

for i in range(kolvo_holod):
    holodilnik.add(input())
recept = int(input())

for i in range(recept):
    name_recept = str(input())
    prod_recept = int(input())
    check = True
    for q in range(prod_recept):
        prod.add(input())
    for w in prod:
        if not w in kolvo_holod:
            check = False

    if check:
        print(name_recept)
    prod = set()
