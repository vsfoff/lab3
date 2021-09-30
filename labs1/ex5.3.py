k1 = int(input("1st: "))
k2 = int(input("2nd: "))

while (k1 or k2) != 0:
    k = int(input("k_")) - 1
    kolvo = int(input("h_m? "))
    if k:
        k2 -= kolvo
        print("\t\t\t", k1, k2)
    else:
        k1 -= kolvo
        print("\t\t\t", k1, k2)

