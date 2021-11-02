n = int(input())
queue = []
for i in range(n):
    s = input().split()
    if 'встал' in s[1]:
        queue.append(s[0])
    elif s[0] == 'Привет,':
        queue.insert(queue.index(s[1][:-1])+1, s[2])
    elif s[1] == 'хватит':
        queue.remove(s[0][:-1])
print(*queue, sep='\n')