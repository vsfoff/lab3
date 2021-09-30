count = int(input())
i = 0
while count != 0:
    i += 1
    if i % 2 == 0:
        if count > 3:
            print("введите количество камней , максимум 3")
        else:
            print("введите кол-во камней ,максимум ", count)
        count -= int(input())
    else:
        if count > 3:
            count -= 3
        else:
            count = 0
if i % 2 == 0:
    print("пользователь выйграл")
else:
    print("выйграл компьютер")
count = int(input())
i = 1
while count != 0:
    if i % 2 == 0:
        if count > 3:
            print("введите количество камней , максимум 3")
        else:
            print("введите кол-во камней ,максимум ", count)
        count -= int(input())
    else:
        if count > 3:
            count -= 3
        else:
            count = 0
    i += 1
if i % 2 == 0:
    print("пользователь выйграл")
else:
    print("выйграл компьютер")
count1 = int(input())
count2 = int(input())
count3 = int(input())
while count2 != 0 or count3 != 0 or count1 != 0:
    n = int(input())
    if n == 1:
        count1 -= int(input())
    elif n == 2:
        count2 -= int(input())
    else:
        count3 -= int(input())
    print(count1, count2, count3)
count1 = int(input())
count2 = int(input())
i = 0
while count1 != 0 or count2 != 0:
    i += 1
    if i % 2 == 0:
        print("введите номер кучи камней ")
        n = int(input())
        if (n == 1):
            while True:
                print("введите кол-во камней ")
                n = int(input())
                if n <= count1:
                    break
            count1 -= n
        else:
            while True:
                print("введите кол-во камней ")
                n = int(input())
                if n <= count2:
                    break
            count2 -= n
    else:
        if count1 != 0:
            count1 = 0
        else:
            count2 = 0
if i % 2 == 0:
    print("пользователь выйграл")
else:
    print("выйграл компьютер")
count1 = int(input())
count2 = int(input())
count3 = int(input())
i = 0
while count1 != 0 or count2 != 0 or count3 != 0:
    i += 1
    if i % 2 == 0:
        print("введите номер кучи ")
        n = int(input())
        if n == 1:
            while True:
                print("введите кол-во камней")
                n = int(input())
                if n <= count1:
                    break
            count1 -= n
        elif n == 2:
            while True:
                print("введите кол-во камней")
                n = int(input())
                if n <= count2:
                    break
            count2 -= n
        else:
            while True:
                print("введите кол-во камней")
                n = int(input())
                if n <= count3:
                    break
            count3 -= n
    else:
        if count1 != 0:
            count1 = 0
        elif count2 != 0:
            count2 = 0
        else:
            count3 = 0
if i % 2 == 0:
    print("выйграл пользователь")
else:
    print("выйграл компьютер")
n = int(input())
for i in range(n, -1, -1):
    print("Осталось секунд:", i)
