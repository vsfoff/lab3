from random import randint

q = int(input('k1:'))
w = int(input('k2:'))


def kuchi(q, w):
    if q > w:
        e = q - w
        q -= e
        a = 1

    elif q < w:
        e = w - q
        w -= e
        a = -1

    else:
        a = 0
        e = randint(0, 1)
        if e:
            q -= 1
        else:
            w -= 1
    return a, q, w


tmp = kuchi(q, w)
q = tmp[1]
w = tmp[2]

print(q, w)
if tmp[0] or tmp[0] == -1:
    while q != 0 and w != 0:
        print('ur step:')
        hm = int(input('hm:'))
        n = int(input('no_k:')) - 1
        if n:  # игрок
            w -= hm
        else:
            q -= hm
        print('k1:', q, 'k2', w)

        if n:  # комп
            q -= hm
        else:
            w -= hm
        print('komp:', q, w)
    else:
        print('u lose')

else:
    hm = int(input('hm:'))
    n = int(input('no_k:')) - 1
    print('ur step:')
    if n:  # игрок
        w -= hm
    else:
        q -= hm
    print('k1:', q, 'k2', w)
    tmp = kuchi(q, w)

    if tmp[0] == -1:
        e = w - q
    elif tmp[0]:
        e = q - w

    if n:  # comp
        q -= e
    else:
        w -= e

    print('comps step:', q, w)

    while q != 0 and w != 0:
        hm = int(input('hm:'))
        n = int(input('no_k:')) - 1
        print('ur step:')
        if n:  # игрок
            w -= hm
        else:
            q -= hm
        print('k1:', q, 'k2', w)

        if q != w:
            if n and q > w:
                e = q - w # comp's step
                q -= e
            elif q < w:
                e = w - q
                w -= e

        else:
            if n:
                q -= e
            else:
                w -= e

        print('comps step:', q, w)

    if q - 1 == -1 and w - 1 == -1:
        print('comp win',)
    elif q - 1 == -1 or w - 1 == -1:
        print('ur step:')
        print(0, 0)
        print('u win')
