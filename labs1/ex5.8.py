hm_k1 = int(input('k1: '))
hm_k2 = int(input('k2: '))
hm_k3 = int(input('k1: '))
a = -1
while hm_k1 < 0 or hm_k1 == 0 or hm_k2 < 0 or hm_k2 == 0 or hm_k3 < 0 or hm_k3 == 0:
    print('Ошибка. Введите значения больше 0')
    hm_k1 = int(input())
    hm_k2 = int(input())
    hm_k3 = int(input())
else:
    while hm_k1 > 0 or hm_k2 > 0 or hm_k3 > 0:
        if a == 1:
            b = 0
            while b < 1 or b > 3:
                b = int(input('Введите номер кучки: '))
            c = 0
            if b == 1:
                hm_k = hm_k1
            elif b == 2:
                hm_k = hm_k2
            elif b == 3:
                hm_k == hm_k3
            while c > hm_k or c < 1:
                c = int(input('Введите количестово: '))
        elif a == -1:
            if hm_k1 - hm_k2 != 0:
                if hm_k1 - hm_k2 > 0:
                    b = 1
                elif hm_k1 - hm_k2 < 0:
                    b = 2
                c = abs(hm_k1 - hm_k2)
            if hm_k1 - hm_k3 != 0:
                if hm_k1 - hm_k3 > 0:
                    b = 1
                elif hm_k1 - hm_k3 < 0:
                    b = 3
                c = abs(hm_k1 - hm_k3)
            if hm_k2 - hm_k3 != 0:
                if hm_k2 - hm_k3 > 0:
                    b = 2
                elif hm_k2 - hm_k3 < 0:
                    b = 3
                c = abs(hm_k2 - hm_k3)
            else:
                b = 1
                c = 1
        if b == 1:
            hm_k1 -= c
        elif b == 2:
            hm_k2 -= c
        elif b == 3:
            hm_k3 -= c
        print(hm_k1, hm_k2, hm_k3)
        a = -a
    if a == -1:
        print('ПОЛЬЗОВАТЕЛЬ выиграл')
    elif a == 1:
        print('КОМПЬЮТЕР выиграл')
