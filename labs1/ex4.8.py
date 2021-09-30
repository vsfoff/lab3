max_count = 0
min = 1
max = 1000
print('500')
vvod = input()
while vvod != '=' and max_count != 10:
    if vvod == '<':
        max = max - (max - min) // 2
        bin = max - (max - min) // 2
        max_count += 1
    if vvod == '>':
        min = min + (max - min) // 2
        bin = min + (max - min) // 2
        max_count += 1
    print("угадал? ", bin)
    vvod = input()