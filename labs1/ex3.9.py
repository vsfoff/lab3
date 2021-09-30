message = input("введите сообщение: ")

count = len(message) * 40
cop = count % 100
rub = count // 100

print(rub, "r.", cop, "k.")
