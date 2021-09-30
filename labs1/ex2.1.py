levo = 1
pravo = 2
pryamo = 3

print("1 - налево, 2 - направо, 3 - прямо\n")
vvod = int(input("каков твой путь ниндзя... "))

if vvod == levo:
    print("здесь можно пойти прямо или направо")
    vvod2 = int(input())
    if vvod2 == pryamo:
        print("поздравляю, вы прошли игру")
    else:
        print("тут даже изолента не поможет")
elif vvod == pryamo:
    print("направо или налево")
    vvod2 = int(input())
    if vvod2 == pravo:
        print("поздравляю, вы прошли игру")
    else:
        print("настоящие пацаны налево не ходят")
elif vvod == pravo:
    print("прямо или налево")
    vvod2 = int(input())
    if vvod2 == levo:
        print("поздравляю, вы прошли игру")
    else:
        print("тебя сожрали долги")
