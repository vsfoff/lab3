def ask_password():
    for i in range(0, 3):
        passwd = input()
        if passwd == 'password':
            print('y')
            break
        elif i == 2:
            print('n')

# ask_password()