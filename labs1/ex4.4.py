passwd = input("введите пароль: ")

if len(passwd) < 8:
    print("короткий пароль")
    quit()
elif passwd.find("123") != -1:
    print("простой")
    quit()
passwd2 = input("повторите пароль: ")

if passwd != passwd2:
    print("различаются")
    quit()
else:
    print("ok")
