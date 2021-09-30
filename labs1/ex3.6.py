code = int(input("введите код: "))
a = len(set(code))

if a == 3:
    print("ok")
if a == 2:
    print("двойное повторение")
if a == 1:
    print("все одинаковое")
