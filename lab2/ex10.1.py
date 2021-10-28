s = input('mess: ')
n = int(input('num: '))
if 0 < n <= len(s):
    print(s[n-1])
else:
    print('err')
