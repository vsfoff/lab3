string = input()
string = string.upper()
k = 0
for i in range(0, len(string)):
    if string.count(string[i]) > k:
        k = string.count(string[i])
print(k)