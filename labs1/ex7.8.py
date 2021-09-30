num = int(input())
onetwo = ['раз', 'два', 'три', 'четыре']
jum = 0
while num > 0:
    for i in range(4):
        word = input()
        if word != onetwo[i]:
            print('Правильных отсчётов было', jum, ', но теперь вы ошиблись.')
            jum = 0
            num -= 1
            break
        jum += 1
print('На сегодня хватит.')