price = int(input())
a = list()
while price != 0:
    a.append(price)
    price = int(input())
for i in range(2,len(a)):
    if a[i-2] > a[i-1] < a[i]:
        inprice = a[i]
        buypos = i
        break
for k in range(buypos+2,len(a)):
    if a[k-2] < a[k-1] > a[k]:
        outprice = a[k]
        break
print(inprice, outprice, outprice - inprice)