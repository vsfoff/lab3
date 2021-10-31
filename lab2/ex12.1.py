n_white = int(input())
white_list = []

for i in range(n_white):
    white_list.append(input())

black = []
n_black = int(input())

for j in range(n_black):
    black.append(input())
for a in black:
    if a in white_list:
        print(a)
