year = int(input("введите год: "))

if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print("високостный")
else:
    print("пшел отседа")
print(year/4)
print(year/100)
print(year/400)