k1 = int(input('k1:'))
k2 = int(input('k2:'))
k3 = int(input('k3:'))

while not (k1 == 0 and k2 == 0 and k3 == 0):
    no_k = int(input('no k:'))
    step = int(input('no:'))
    if no_k == 1:
        k1 -= step
    elif no_k == 2:
        k2 -= step
    elif no_k == 3:
        k3 -= step
    print('k1:', k1, 'k2:', k2,'k3:', k3)
