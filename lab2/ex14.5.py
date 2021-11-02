url =[list(i.split("=")) for j in list(input().split("?")) for i in list(j.split("&"))][1:]
key = input()
for i in range(len(url)):
    if url[i][0] == key:
        print(url[i][1])
