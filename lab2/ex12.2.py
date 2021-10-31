s = input()
n = int(s[:4])
total = int(s[4:])
error = []
true = 0

for i in range(n):
    s = input()
    price = int(s[:7])
    amount = int(s[8:12])
    cost = int(s[13:])
    if price * amount != cost:
        error.append(i + 1)
    true += price * amount
print(total - true)
for x in error:
    print(x, end=' ')
