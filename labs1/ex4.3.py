from math import log

n = int(input("число: "))

logn = log(n, 2)
if logn == int(logn):
    print(int(logn))
else:
    print("no")
