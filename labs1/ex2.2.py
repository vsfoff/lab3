login = str(input("введите логин: "))


while "@" in login:
    print("была введена почта, повтори попытку ", end='')
    login = input()
else:
    print("введеный логин: ", login)

email = input("введите резервную почту ")

while "@" not in email:
    print("просьба ввести почту ", end='')
    email = input()
else:
    print("введеная почта: ", email)