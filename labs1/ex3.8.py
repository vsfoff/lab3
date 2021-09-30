passwd = str(input("введите пароль: "))

q = int(passwd[0]) + int(passwd[1])
w = int(passwd[1]) + int(passwd[2])

if q > w:
    print(str(q) + str(w))
else:
    print(str(w) + str(q))

