n = int(input())
ingridient = []
for i in range(n):
    enter = input()
    if 'лук' not in enter:
        ingridient.append(enter)
print(' ,'.join(ingridient))

