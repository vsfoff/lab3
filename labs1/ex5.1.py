d = int(input("data: "))
m = int(input("month: "))
year = int(input("year: "))

c = int(year / 100)
y = ((year - c) % 100)

ab = d + ((13*m - 1) // 5) + y + (y // 4 + c // 4 - 2*c + 777)
ab %= 7

print(int(ab))
