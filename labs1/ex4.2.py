q = w = 0
while True:
    temp = float(input("введите температуру:"))
    if temp > 0:
        q += 1
        w += temp
    elif temp < -300:
        print(w / q)
        quit()


