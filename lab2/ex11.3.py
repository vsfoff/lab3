inp = input().lower()
n = int(input()) - 1
letter = input().lower()
if (0 < n <= len(inp)) and (letter in inp) and (len(letter) == 1):
    print('y') if inp[n] == letter else print('n')
else:
    print('err')
